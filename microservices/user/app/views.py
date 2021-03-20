import json
import jwt

from datetime import datetime
from datetime import timedelta

from flask import Response
from flask import request
from werkzeug.security import check_password_hash

from app import app
from app import db
from app.exceptions import UserExceptions
from app.exceptions import AuthExceptions
from app.user import UserData
from app.models import User
from app.schemas import UserSchema


@app.route("/user", methods=["GET", "POST"])
def user():
    try:
        if request.method == "POST":
            user_data = UserData(**request.form).__dict__
            user = User(**user_data)
            if not User.query.filter_by(email=user.email).first():
                db.session.add(user)
                db.session.commit()
        response = UserSchema(many=True).dump(User.query.all())
        return Response(json.dumps(response), mimetype='application/json')
    except Exception as e:
        print(f"Error: {e}")
        return Response(json.dumps(UserExceptions.ERROR.value), mimetype='application/json')


@app.route("/auth", methods=["POST"])
def auth():
    try:
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return Response(json.dumps(AuthExceptions.AUTH_NOT_FOUND.value), mimetype='application/json')
            
        user = User.query.filter_by(username=auth.username).first()
        if not user:
            return Response(json.dumps(AuthExceptions.USER_NOT_FOUND.value), mimetype='application/json')

        if not check_password_hash(user.password, auth.password):
            return Response(json.dumps(AuthExceptions.PASSWORD_NOT_MATCH.value), mimetype='application/json')
        response = {
            "token": jwt.encode(UserSchema().dump(user), app.config['SECRET_KEY'], 'HS256'),
            "expired": datetime.timestamp(datetime.now() + timedelta(hours=12))
        }
        return Response(json.dumps(response), mimetype='application/json')
    except Exception as e:
        print(f"Error: {e}")
        return Response(json.dumps(AuthExceptions.ERROR.value), mimetype='application/json')
