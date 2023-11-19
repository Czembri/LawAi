
from flask import Blueprint, request, jsonify
from AI.constitution import ConstitutionAI
from API import app

from shared.auth_decorator import require_secret_header

constitution = Blueprint('constitution', __name__)

@app.route("/api/v1/constitution-ai/load-data", methods=["GET"])
@require_secret_header
def constitution_AI_data():
    global ai_instance2
    ai_instance2 = _get_c_data()
    return jsonify({
        'message': 'Data loaded successfully'
    })

@app.route("/api/v1/constitution-ai", methods=["POST"])
@require_secret_header
def constitution_AI():
    data = request.get_json()
    data_query = data["query"]
    return jsonify({
        'response': ai_instance2.get_response(data_query)
    })

@app.route("/api/v1/constitution-ai/clear-memory", methods=["GET"])
@require_secret_header
def clear_c_memory():
    ai_instance2.clear_memory()
    return jsonify({
        'response': 'Memory cleared'
    })

def _get_c_data():
    ai = ConstitutionAI()
    ai.load_data()
    return ai