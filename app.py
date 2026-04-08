import streamlit as st
import json
from graph.workflow import build_workflow
from utils.preprocessor import preprocess_input

# -------------------- CONFIG --------------------
st.set_page_config(page_title="FlowMind AI", layout="wide")

# -------------------- UI STYLE --------------------
st.markdown("""
<style>
.stApp {
    background-color: #eef2f7;
    color: #111827;
}
textarea {
    background-color: #ffffff !important;
    color: #000000 !important;
}
.stButton button {
    background-color: #2563eb;
    color: white;
    border-radius: 10px;
    padding: 0.5rem 1.2rem;
}
</style>
""", unsafe_allow_html=True)

# -------------------- LOG RESET --------------------
def reset_logs():
    with open("data/logs.json", "w") as f:
        json.dump([], f)

# -------------------- HEADER --------------------
st.title("FlowMind AI")
st.caption("Autonomous Multi-Agent Workflow Engine")

# -------------------- INPUT --------------------
uploaded_file = st.file_uploader("Upload Transcript (.txt / .md)", type=["txt", "md"])

if uploaded_file:
    input_text = uploaded_file.read().decode("utf-8")
else:
    input_text = st.text_area(
        "Enter Task / Transcript",
        height=150,
        placeholder="Example: Assign backend to John and launch feature by Friday"
    )

# -------------------- RUN --------------------
if st.button("Run Workflow"):

    reset_logs()

    chunks = preprocess_input(input_text)

    app = build_workflow()

    all_tasks, all_steps = [], []
    all_issues, all_fixes = [], []
    agent_trace = []
    final_status = "PASS"

    for chunk in chunks:
        try:
            result = app.invoke({"input": chunk})
        except Exception as e:
            st.error(f"Error: {str(e)}")
            continue

        all_tasks.extend(result.get("tasks", []))
        all_steps.extend(result.get("steps", []))

        if result.get("status") == "FAIL":
            final_status = "FAIL"
            all_issues.extend(result.get("issues", []))

        if result.get("recovery"):
            all_fixes.extend(result.get("recovery"))

        try:
            with open("data/logs.json") as f:
                agent_trace = json.load(f)
        except:
            pass

    # -------------------- OUTPUT --------------------

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Tasks")
        st.json(all_tasks)

    with col2:
        st.markdown("### Steps")
        st.json(all_steps)

    st.markdown("### Validation Status")

    if final_status == "FAIL":
        st.error("FAIL")
    else:
        st.success("PASS")

    # ---------- ISSUES ----------
    if final_status == "FAIL":
        st.markdown("### Issues")
        st.write(all_issues)

    # ---------- FIXES ----------
    if all_fixes:
        st.markdown("### Auto Fixes Applied")

        for fix in all_fixes:
            st.write(f"• {fix['task']}")
            st.caption(f"Issue: {fix['problem']}")
            st.caption(f"Fix: {fix['suggested_fix']}")
            st.markdown("---")

        if final_status == "FAIL":
            st.warning("System suggests fixes but workflow still needs attention")
        else:
            st.success("Workflow completed after auto-corrections")

    elif final_status == "PASS":
        st.success("Workflow executed successfully")

    # ---------- AGENT TRACE ----------
    with st.expander("Agent Decision Flow"):
        for log in agent_trace:
            st.write(f"**{log['step'].upper()}**")
            st.json(log["data"])
            st.markdown("---")