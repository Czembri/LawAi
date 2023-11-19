from API import app
from _config import constants
import os
from API.document_generator_api import document_generator
from API.law_ai_api import law_ai
from API.constitution_api import constitution

app.register_blueprint(document_generator)
app.register_blueprint(law_ai)
app.register_blueprint(constitution)

if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = constants.API_KEY
    os.environ["JWT_AUTH"] = constants.JWT_AUTH
    os.environ["SECRET_KEY"] = constants.SECRET_KEY
    app.run(debug=True, port=8001)