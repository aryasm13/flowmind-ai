import streamlit as st
import json
from graph.workflow import build_workflow
from utils.preprocessor import preprocess_input

# -------------------- CONFIG --------------------
st.set_page_config(
    page_title="FlowMind AI",
    layout="wide"
)

# -------------------- LIGHT THEME STYLE --------------------
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
st.write("Provide a business instruction or upload a transcript. The system will process and execute the workflow.")

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

# -------------------- RUN WORKFLOW --------------------
if st.button("Run Workflow"):

    reset_logs()  # clear logs every run

    app = build_workflow()

    clean_text = preprocess_input(input_text)

    # Optional visibility
    with st.expander("Processed Input"):
        st.write(clean_text)

    result = app.invoke({"input": clean_text})

    # -------------------- OUTPUT --------------------

    st.subheader("Extracted Tasks")
    st.json(result.get("tasks"))

    st.subheader("Planned Steps")
    st.json(result.get("steps"))

    st.subheader("Validation Status")
    st.write(result.get("status"))

    if result.get("status") == "FAIL":
        st.subheader("Issues Detected")
        st.write(result.get("issues"))

        st.subheader("Recovery Actions")
        st.json(result.get("recovery"))
    else:
        st.success("Workflow executed successfully")