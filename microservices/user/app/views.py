import json
import jwt

from datetime import datetime
from datetime import timedelta

from flask import Response
from flask import request
from werkzeug.security import check_password_hash

from app import app
from app import db
from app import metrics
from app.exceptions import UserExceptions
from app.exceptions import AuthExceptions
from app.user import UserData
from app.models import User
from app.schemas import UserSchema
from app.prometheus import user_counter
from app.prometheus import auth_counter


@app.route('/user', methods=["POST"])
@user_counter
def user():
    try:
        user = User(**UserData(**request.form).__dict__)
        if not User.query.filter_by(email=user.email).first():
            db.session.add(user)
            db.session.commit()
            return Response(json.dumps({
                "status": True,
                "response_data": UserSchema().dump(user)
            }), mimetype='application/json')
        return Response(json.dumps({
            "status": False,
            "response_data": UserSchema(many=True).dump(User.query.all())
        }), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({
            "status": False,
            "error": UserExceptions.ERROR.value.format(str(e))
        }), mimetype='application/json')


@app.route('/user/<user_id>', methods=["GET"])
@user_counter
def user_by_id(user_id):
    try:
        if not user_id:
            return Response(json.dumps({
                "status": False,
                "error": UserExceptions.USER_ID_IS_MISSING.value
            }), mimetype='application/json')
        user = User.query.filter_by(id=user_id).first()
        if not user:
            return Response(json.dumps({
                "status": False,
                "error": UserExceptions.USER_ID_NOT_FOUND.value.format(user_id)
            }), mimetype='application/json')
        return Response(json.dumps({
            "status": True,
            "response_data": UserSchema().dump(user)
        }), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({
            "status": False,
            "error": UserExceptions.ERROR.value.format(str(e))
        }), mimetype='application/json')


@app.route('/user/auth', methods=["POST"])
@auth_counter
def auth():
    try:
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return Response(json.dumps({
                "status": False,
                "error": AuthExceptions.AUTH_NOT_FOUND.value
            }), mimetype='application/json')
        user = User.query.filter_by(username=auth.username).first()
        if not user:
            return Response(json.dumps({
                "status": False,
                "error": AuthExceptions.USER_NOT_FOUND.value
            }), mimetype='application/json')
        if not check_password_hash(user.password, auth.password):
            return Response(json.dumps({
                "status": False,
                "error": AuthExceptions.PASSWORD_NOT_MATCH.value
            }), mimetype='application/json')
        return Response(json.dumps({
            "status": True,
            "response_data": {
                "token": jwt.encode(UserSchema().dump(user), app.config['SECRET_KEY']),
                "expired": datetime.timestamp(datetime.now() + timedelta(hours=12))
            }
        }), mimetype='application/json')
    except Exception as e:
        return Response(json.dumps({
            "status": False,
            "error": AuthExceptions.ERROR.value.format(str(e))
        }), mimetype='application/json')
