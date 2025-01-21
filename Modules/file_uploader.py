import os
from flask import Blueprint, request, jsonify

file_uploader_blueprint = Blueprint('file_uploader', __name__)
UPLOAD_FOLDER = './static/uploads/'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'docx'}

def allowed_file(filename):
    """
    Check if the file extension is allowed.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@file_uploader_blueprint.route('/upload', methods=['POST'])
def upload_file():
    """
    Handle file upload and save it to the server.
    """
    if 'file' not in request.files:
        return jsonify({"message": "No file provided"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"message": "No file selected"}), 400

    if file and allowed_file(file.filename):
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)
        return jsonify({"message": "File uploaded successfully", "path": file_path}), 200

    return jsonify({"message": "File type not allowed"}), 400
