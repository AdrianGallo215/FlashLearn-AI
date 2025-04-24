from ..main import app
from ..services.file_processor import File_Processor
from flask import request, jsonify

file_processor = File_Processor()

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'files' not in request.files:
        return jsonify({'error': "No 'files' part in the request"}), 400
    files = request.files.getlist('files')

    if not files or all(file.filename == '' for file in files):
        return jsonify({'error': "No selected files"}), 400

    successful_files = []
    failed_files = []

    for file in files:
        success, message = file_processor.save_file(file)

        if result:
            successful_files.append({'filename': file.filename, 'path': message})
        else:
            failed_files.append({'filename': file.filename, 'error': message})

    overall_status = "success"
    status_code = 200

    if failed_files:
        if successful_files:
            overall_status = "partial_success"
        else:
            overall_status = "failure"
            status_code = 400
    
    return jsonify({
        'status': overall_status,
        'successful_files': successful_files,
        'failed_files': failed_files
    }), status_code
            

