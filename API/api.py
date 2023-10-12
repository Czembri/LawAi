from flask import Blueprint, request
from API import app
from AI.constitution import ConstitutionAI

routes = Blueprint('routes', __name__)

@app.route("/api/v1/constitution-ai", methods=["GET", "POST"])
def constitutionAI():
    data = request.get_json()
    ai = ConstitutionAI(data["query"])
    return ai.getResponse()