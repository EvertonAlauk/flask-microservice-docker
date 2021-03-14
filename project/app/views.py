import json

from flask import Response
from flask import request

from app import app
from app import db
from app.models import User
from app.schemas import UserSchema


@app.route("/user", methods=["GET", "POST"])
def users():
    try:
        if request.method == "POST":
            user = User(email=request.form.get('email'))
            queryset = User.query.filter_by(email=user.email).first()
            if not queryset:
                db.session.add(user)
                db.session.commit()
        response = UserSchema(many=True).dump(User.query.all())
        return Response(json.dumps(response),  mimetype='application/json')
    except Exception as e:
        print(f"Error: {e}")
    response = {"error": "Error in user API."}
    return Response(json.dumps(response),  mimetype='application/json')