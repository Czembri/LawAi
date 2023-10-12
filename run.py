from API import app
from API.api import routes
from _config import constants
import os

app.register_blueprint(routes, url_prefix="")

if __name__ == "__main__":
    
    os.environ["OPENAI_API_KEY"] = constants.API_KEY    
    app.run(debug=True)