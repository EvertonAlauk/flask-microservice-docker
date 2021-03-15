import jwt
import json
from functools import wraps

from flask import request
from flask import Response

from app import app
from app.models import User


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return Response(json.dumps({"error": "Token is missing."}), mimetype='application/json')
        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            user = User.query.filter(User.username==data['username'])
        except Exception as e:
            print(f"Error: {e}")
            return Response(json.dumps({"error": "Error in token required decorator."}), mimetype='application/json')
        return f(user, *args, **kwargs)
    return decorated