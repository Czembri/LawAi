from flask import Blueprint, request, jsonify
from AI.document_analyzer import DocumentAnalyzer
from API import app
from shared.auth_decorator import require_secret_header

document_analyzer = Blueprint('document_analyzer', __name__)

@app.route("/api/v1/document-analyzer", methods=["POST"])
@require_secret_header
def analyze_document():
    ai_instance = DocumentAnalyzer()
    data = request.get_json()
    data_query = data["query"]
    response = ai_instance.analyze_document(data_query)
    
    return jsonify({
        'response': response
    })
