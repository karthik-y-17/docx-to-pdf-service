import os
import pythoncom
from win32com import client

def convert_docx_to_pdf(input_path: str, output_path: str) -> str:
    """
    Converts DOCX to PDF using Microsoft Word COM automation.
    Works only on Windows with MS Word installed.
    Handles multithreaded Flask requests.
    """
    if not os.path.exists(input_path):
        raise FileNotFoundError("Input DOCX not found")

    # Initialize COM for this thread
    pythoncom.CoInitialize()

    word = client.Dispatch("Word.Application")
    word.Visible = False

    try:
        doc = word.Documents.Open(os.path.abspath(input_path))
        doc.SaveAs(os.path.abspath(output_path), FileFormat=17)  # 17 = PDF
        doc.Close()
    finally:
        word.Quit()
        pythoncom.CoUninitialize()  # Clean up COM

    if not os.path.exists(output_path):
        raise Exception("PDF conversion failed")

    return output_path
