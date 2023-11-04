from API import app
from _config import constants
import os
from API.law_ai_api import routes

app.register_blueprint(routes, url_prefix="")

if __name__ == "__main__":
    os.environ["OPENAI_API_KEY"] = constants.API_KEY    
    app.run(debug=True, port=8001)