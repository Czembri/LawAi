from flask import Flask
from flask_cors import CORS
import os

from flask_jwt_extended import JWTManager

app = Flask(__name__)
CORS(app)
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
jwt = JWTManager(app)

app.config['JWT_SECRET_KEY'] =  os.getenv("JWT_AUTH")
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

## JWT CONFIG
# app.config['JWT_TOKEN_LOCATION'] = ['headers']
# app.config['JWT_HEADER_NAME'] = 'Authorization'
# app.config['JWT_HEADER_TYPE'] = 'Bearer'

app.config.from_object(__name__)