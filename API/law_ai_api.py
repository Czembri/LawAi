from flask import Blueprint, request, jsonify
from AI.constitution import ConstitutionAI
from AI.law_ai import LawAI
from API import app

routes = Blueprint('routes', __name__)

@app.route("/api/v1/law-ai/load-data", methods=["GET"])
def law_AI_data():
    global ai_instance
    ai_instance = _get_data()
    return jsonify({
        'message': 'Data loaded successfully'
    })

@app.route("/api/v1/law-ai", methods=["POST"])
def law_AI():
    data = request.get_json()
    data_query = data["query"]
    return jsonify({
        'response': ai_instance.generate(data_query)
    })

@app.route("/api/v1/law-ai/clear-memory", methods=["GET"])
def clear():
    ai_instance.clear()
    return jsonify({
        'response': 'Memory cleared'
    })

@app.route("/api/v1/law-ai/get-messages", methods=["GET"])
def get_messages():
    return jsonify({
        'response': ai_instance.get_messages()
    })

def _get_data():
    ai = LawAI()
    return ai



### CONSTITUTUION API ###

@app.route("/api/v1/constitution-ai/load-data", methods=["GET"])
def constitution_AI_data():
    global ai_instance2
    ai_instance2 = _get_c_data()
    return jsonify({
        'message': 'Data loaded successfully'
    })

@app.route("/api/v1/constitution-ai", methods=["POST"])
def constitution_AI():
    data = request.get_json()
    data_query = data["query"]
    return jsonify({
        'response': ai_instance2.get_response(data_query)
    })

@app.route("/api/v1/constitution-ai/clear-memory", methods=["GET"])
def clear_c_memory():
    ai_instance2.clear_memory()
    return jsonify({
        'response': 'Memory cleared'
    })

def _get_c_data():
    ai = ConstitutionAI()
    ai.load_data()
    return ai