from flask import Flask, request, send_file, jsonify, render_template
from converter.docx_converter import convert_docx_to_pdf
from utils.file_utils import save_uploaded_file, get_output_pdf_path

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("upload.html")


@app.route("/convert", methods=["POST"])
def convert_file():
    try:
        # Check uploaded file
        if "file" not in request.files:
            return jsonify({"error": "No file uploaded"}), 400

        file = request.files["file"]

        if not file.filename.endswith(".docx"):
            return jsonify({"error": "Only .docx allowed"}), 400

        # Save file & define output
        input_path = save_uploaded_file(file)
        output_path = get_output_pdf_path(input_path)

        # Convert DOCX → PDF
        convert_docx_to_pdf(input_path, output_path)

        # Send PDF back to browser
        return send_file(output_path, as_attachment=True)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
