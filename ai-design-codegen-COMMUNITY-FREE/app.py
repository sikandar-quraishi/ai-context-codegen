import streamlit as st
from project_analyzer import extract_project, analyze_structure
from ai_engine import detect_layout_type, generate_code

st.set_page_config(page_title="AI Design Code Generator FREE", layout="wide")

st.title("🚀 AI Design → Code Generator (Community FREE Version)")

framework = st.selectbox(
    "Select Framework",
    ["React", "Vue.js", "Angular"]
)

st.markdown("### 📦 Upload Existing Project (Optional)")
project_zip = st.file_uploader("Upload ZIP File", type=["zip"])

components = []

if project_zip:
    path = extract_project(project_zip)
    components = analyze_structure(path)
    st.success("Project analyzed successfully ✅")
    st.write("Detected Components:")
    st.write(components)

st.markdown("### 🎨 Upload UI Screenshot (Optional)")
design_image = st.file_uploader("Upload Design Image", type=["png", "jpg", "jpeg"])

layout_type = "dashboard"

if design_image:
    layout_type = detect_layout_type(design_image.name)

if st.button("Generate Code 🚀"):
    code = generate_code(framework, layout_type, components)

    st.subheader("💻 Generated Code")
    st.code(code, language="javascript")

    st.download_button(
        "Download File",
        code,
        file_name="GeneratedComponent.js"
    )
