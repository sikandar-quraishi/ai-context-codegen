import zipfile
import os
import shutil

EXTRACT_PATH = "temp_project"

def extract_project(uploaded_zip):
    if os.path.exists(EXTRACT_PATH):
        shutil.rmtree(EXTRACT_PATH)

    os.makedirs(EXTRACT_PATH, exist_ok=True)

    with zipfile.ZipFile(uploaded_zip, 'r') as zip_ref:
        zip_ref.extractall(EXTRACT_PATH)

    return EXTRACT_PATH


def analyze_structure(project_path):
    summary = []

    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.endswith((".js", ".jsx", ".ts", ".tsx", ".vue")):
                relative_path = os.path.relpath(
                    os.path.join(root, file), project_path
                )
                summary.append(relative_path)

    return summary[:30]
