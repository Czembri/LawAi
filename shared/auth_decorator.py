from flask import request, jsonify
from functools import wraps
from API import app

def require_secret_header(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        secret_header_value = request.headers.get('X-App-Key')
        expected_secret_value = app.config["SECRET_KEY"]

        if secret_header_value != expected_secret_value:
            return jsonify({"error": "Invalid or missing secret header"}), 403

        return f(*args, **kwargs)

    return decorated_function
