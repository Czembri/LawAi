from flask import Blueprint, request, jsonify
from API import app
from AI.constitution import ConstitutionAI

routes = Blueprint('routes', __name__)

@app.route("/api/v1/constitution-ai", methods=["GET", "POST"])
def constitutionAI():
    data = request.get_json()
    ai = ConstitutionAI(data["query"])
    return jsonify({
        'response': ai.getResponse()
    })