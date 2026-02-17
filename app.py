import streamlit as st
from project_analyzer import extract_project, analyze_structure
from ai_engine import generate_code

st.set_page_config(page_title="AI Context Code Generator", layout="wide")

st.title("🚀 AI Context-Aware Design → Code Generator (Full Demo)")

framework = st.selectbox(
    "Select Framework",
    ["React", "Vue.js", "Angular"]
)

st.markdown("### 📦 Upload Existing Project (ZIP)")
project_zip = st.file_uploader("Upload ZIP File", type=["zip"])

project_structure = None

if project_zip:
    path = extract_project(project_zip)
    project_structure = analyze_structure(path)
    st.success("Project analyzed successfully ✅")
    st.write("Detected Files:")
    st.write(project_structure)

st.markdown("### 🎨 Upload New UI Design Image")
design_image = st.file_uploader("Upload Design Image", type=["png", "jpg", "jpeg"])

if design_image and st.button("Generate Code 🚀"):
    with st.spinner("Generating context-aware code..."):
        image_bytes = design_image.read()
        generated_code = generate_code(
            image_bytes,
            framework,
            project_structure
        )

        st.subheader("💻 Generated Code")
        st.code(generated_code, language="javascript")

        st.download_button(
            "Download File",
            generated_code,
            file_name="NewScreenComponent.js"
        )
