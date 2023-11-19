from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from AI.document_generator import DocumentGenerator
from API import app
from shared.auth_decorator import require_secret_header

document_generator = Blueprint('document_generator', __name__)

@app.route("/api/v1/document-generator", methods=["POST"])
@require_secret_header
def post_document_info():
    ai_instance = DocumentGenerator()
    data = request.get_json()
    data_query = data["query"]
    response = ai_instance.generate_document(data_query)
    
    return jsonify({
        'response': response
    })
