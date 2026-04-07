import streamlit as st
import json
from graph.workflow import build_workflow
from utils.preprocessor import preprocess_input

# -------------------- CONFIG --------------------
st.set_page_config(
    page_title="FlowMind AI",
    layout="wide"
)

# -------------------- LIGHT UI --------------------
st.markdown("""
    <style>
    .stApp {
        background-color: #f5f7fb;
        color: #1f2937;
    }

    textarea, .stTextArea textarea {
        background-color: #ffffff !important;
        color: #000000 !important;
    }

    .stButton button {
        background-color: #2563eb;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }

    .stButton button:hover {
        background-color: #1d4ed8;
    }
    </style>
""", unsafe_allow_html=True)

# -------------------- LOG RESET --------------------
def reset_logs():
    with open("data/logs.json", "w") as f:
        json.dump([], f)

# -------------------- HEADER --------------------
st.title("FlowMind AI - Autonomous Workflow Agent")
st.write("Provide a business instruction or upload a transcript to run the workflow.")

# -------------------- INPUT --------------------
uploaded_file = st.file_uploader("Upload Transcript (.txt / .md)", type=["txt", "md"])

input_text = ""

if uploaded_file is not None:
    input_text = uploaded_file.read().decode("utf-8")
    st.success("File uploaded successfully")
else:
    input_text = st.text_area(
        "Enter Task:",
        "Assign backend to John and launch feature by Friday"
    )

# -------------------- RUN --------------------
if st.button("Run Workflow"):

    reset_logs()

    chunks = preprocess_input(input_text)

    with st.expander("Processed Input Chunks"):
        st.write(chunks)

    app = build_workflow()

    all_tasks = []
    all_steps = []
    all_issues = []
    all_fixes = []
    final_status = "PASS"

    for chunk in chunks:
        try:
            result = app.invoke({"input": chunk})
        except Exception as e:
            st.error(f"Error in chunk processing: {str(e)}")
            continue

        # Aggregate
        all_tasks.extend(result.get("tasks", []))
        all_steps.extend(result.get("steps", []))

        if result.get("status") == "FAIL":
            final_status = "FAIL"
            all_issues.extend(result.get("issues", []))
            fixes = result.get("recovery", {}).get("fixes", [])
            all_fixes.extend(fixes)

    # -------------------- OUTPUT --------------------

    st.subheader("Extracted Tasks")
    st.json(all_tasks)

    st.subheader("Planned Steps")
    st.json(all_steps)

    st.subheader("Validation Status")
    st.write(final_status)

    if final_status == "FAIL":
        st.subheader("Issues Detected")
        st.write(all_issues)

        st.subheader("Recovery Actions")
        st.json(all_fixes)
    else:
        st.success("Workflow executed successfully")