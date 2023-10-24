from flask import Blueprint, request, jsonify
from API import app
from AI.constitution import ConstitutionAI

routes = Blueprint('routes', __name__)


@app.route("/api/v1/constitution-ai/load-data", methods=["GET"])
def constitution_AI_data():
    global ai_instance
    ai_instance = _get_data()
    return jsonify({
        'message': 'Data loaded successfully'
    })

@app.route("/api/v1/constitution-ai", methods=["POST"])
def constitution_AI():
    data = request.get_json()
    data_query = data["query"]
    return jsonify({
        'response': ai_instance.get_response(data_query)
    })

@app.route("/api/v1/constitution-ai/clear-memory", methods=["GET"])
def clear():
    ai_instance.clear_memory()
    return jsonify({
        'response': 'Memory cleared'
    })

def _get_data():
    ai = ConstitutionAI()
    ai.load_data()
    return ai