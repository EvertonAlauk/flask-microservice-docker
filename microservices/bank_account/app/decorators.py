import jwt
import json
from functools import wraps

from flask import request
from flask import Response

from app import app

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = str(request.headers['Authorization']).replace('Bearer ', '')
        if not token:
            return Response(json.dumps({"error": "Token is missing."}), mimetype='application/json')
        try:
            data = jwt.decode(
                jwt=token,
                secret=app.config['SECRET_KEY'],
                algorithms=["HS256"],
                options={"verify_signature": False}
            )
        except Exception as e:
            print(f"Error: {e}")
            return Response(json.dumps({"error": "Error in token required decorator."}), mimetype='application/json')
        return f(data.get("id"), *args, **kwargs)
    return decorated
