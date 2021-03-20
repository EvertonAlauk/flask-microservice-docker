import json
from decimal import Decimal

from flask import Response
from flask import request

from app import app
from app import db
from app.models import Credit
from app.schemas import CreditSchema
from app.decorators import token_required

@app.route("/credit", methods=["POST"])
@token_required
def credit(user_id):
    credit = Credit(
        user_id=int(user_id),
        credit=request.form.get('credit')
    )
    db.session.add(credit)
    db.session.commit()
    response = CreditSchema().dump(credit)
    return Response(json.dumps(response), mimetype='application/json')
