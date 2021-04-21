import jwt
import json
from functools import wraps

from flask import request
from flask import Response

from app.exceptions import AuthExceptions
from app.exceptions import BankAccountExceptions
from app.models import Balance

from app import app

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = str(request.headers['Authorization']).replace('Bearer ', '')
        if not token:
            return Response(json.dumps({
                "status": False,
                "error": AuthExceptions.JWT_NOT_FOUND.value
            }), mimetype='application/json')
        try:
            data = jwt.decode(
                jwt=token,
                secret=app.config['SECRET_KEY'],
                algorithms=["HS256"],
                options={"verify_signature": False}
            )
        except Exception as e:
            return Response(json.dumps({
                "status": False,
                "error": AuthExceptions.ERROR.value.format(str(e))
            }), mimetype='application/json')
        user_id = int(data['user']['id'])
        return f(user_id, *args, **kwargs)
    return decorated
