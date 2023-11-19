from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from AI.law_ai import LawAI
from API import app
from shared.auth_decorator import require_secret_header

law_ai = Blueprint('law_ai', __name__)

@app.route("/api/v1/law-ai/load-data", methods=["GET"])
@require_secret_header
def law_AI_data():
    global ai_instance
    ai_instance = _get_data()
    return jsonify({
        'message': 'Data loaded successfully'
    })

@app.route("/api/v1/law-ai", methods=["POST"])
@require_secret_header
def law_AI():
    data = request.get_json()
    data_query = data["query"]
    return jsonify({
        'response': ai_instance.generate(data_query)
    })

@app.route("/api/v1/law-ai/clear-memory", methods=["GET"])
@require_secret_header
def clear():
    ai_instance.clear()
    return jsonify({
        'response': 'Memory cleared'
    })

@app.route("/api/v1/law-ai/get-messages", methods=["GET"])
@require_secret_header
def get_messages():
    return jsonify({
        'response': ai_instance.get_messages()
    })

def _get_data():
    ai = LawAI()
    return ai
