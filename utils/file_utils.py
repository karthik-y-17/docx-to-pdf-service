import os
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "outputs"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def save_uploaded_file(file):
    """Save uploaded file to uploads/ folder"""
    filename = secure_filename(file.filename)
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    file.save(input_path)
    return input_path

def get_output_pdf_path(input_path):
    """Generate output PDF path based on input DOCX"""
    base = os.path.splitext(os.path.basename(input_path))[0]
    return os.path.join(OUTPUT_FOLDER, base + ".pdf")
