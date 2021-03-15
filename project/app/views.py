import json
import jwt
import datetime
from datetime import datetime as dt

from flask import Response
from flask import request
from flask import json
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from app import app
from app import db
from app.models import User
from app.schemas import UserSchema
from app.decorators import token_required


@app.route("/auth", methods=["POST"])
def auth():
    try:
        auth = request.authorization
        if not auth or not auth.username or not auth.password:
            return Response(json.dumps({"error": "Auth not verified."}), mimetype='application/json')

        user = User.query.filter(User.username==auth.username).one()
        if not user:
            return Response(json.dumps({"error": "User not found."}), mimetype='application/json')

        if user and check_password_hash(user.password, auth.password):
            expired = datetime.datetime.now() + datetime.timedelta(hours=12)

            token = jwt.encode({
                'username': user.username,
                'expired': dt.timestamp(expired)
            }, app.config['SECRET_KEY'])
            
            response = {
                "message": "Auth validated.",
                "token": token,
                "expired": dt.timestamp(expired)
            }
            return Response(json.dumps(response), mimetype='application/json')
    except Exception as e:
        print(f"Error: {e}")
    return Response(json.dumps({"error": "Error in auth API."}), mimetype='application/json')


@app.route("/user", methods=["GET", "POST"])
def users():
    try:
        if request.method == "POST":
            user = User(
                username=request.form.get('username'),
                email=request.form.get('email'),
                password=generate_password_hash(request.form.get('password')),
                name=request.form.get('name')
            )
            queryset = User.query.filter_by(email=user.email).first()
            if not queryset:
                db.session.add(user)
                db.session.commit()

        response = UserSchema(many=True).dump(User.query.all())
        return Response(json.dumps(response), mimetype='application/json')
    except Exception as e:
        print(f"Error: {e}")
    return Response(json.dumps({"error": "Error in user API."}), mimetype='application/json')


@app.route("/credit", methods=["GET"])
@token_required
def credit():
    return Response({}, mimetype='application/json')
