from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG

app.config['SECRET_KEY'] = '253fc3280dd1d06014911ee6dcde4382'
app.config.from_object(__name__)

from API import api