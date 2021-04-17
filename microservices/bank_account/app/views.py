import json
from decimal import Decimal

from flask import Response
from flask import request

from app import app
from app import db
from app.models import Credit
from app.models import Debit
from app.models import Balance
from app.schemas import CreditSchema
from app.schemas import DebitSchema
from app.schemas import BalanceSchema
from app.decorators import token_required
from app.prometheus import balance_counter
from app.prometheus import credit_counter
from app.prometheus import debit_counter
from app.prometheus import statement_counter


@app.route("/bank_account/credit/", methods=["POST"])
@token_required
@credit_counter
def credit(user_id):
    credit = Credit(
        user_id=int(user_id),
        value=request.form.get('value')
    )
    balance = Balance.query.filter_by(user_id=user_id).first()
    if not balance:
        return Response(json.dumps({"Error": "Balance empty."}), mimetype='application/json')

    balance.value -= float(credit.value)
    db.session.add(balance)
    db.session.add(credit)
    db.session.commit()
    response = CreditSchema().dump(credit)
    return Response(json.dumps(response), mimetype='application/json')


@app.route("/bank_account/debit/", methods=["POST"])
@token_required
@debit_counter
def debit(user_id):
    debit = Debit(
        user_id=int(user_id),
        value=request.form.get('value')
    )
    balance = Balance.query.filter_by(user_id=user_id).first()
    if not balance:
        return Response(json.dumps({"Error": "Balance empty."}), mimetype='application/json')

    balance.value -= float(debit.value)
    db.session.add(balance)
    db.session.add(debit)
    db.session.commit()
    response = DebitSchema().dump(debit)
    return Response(json.dumps(response), mimetype='application/json')


@app.route("/bank_account/balance/", methods=["GET", "POST"])
@token_required
@balance_counter
def balance(user_id):
    if request.method == "POST":
        balance = Balance.query.filter_by(user_id=user_id).first()
        if not balance:
            balance = Balance(
                user_id=int(user_id),
                value=request.form.get('value')
            )
        else:
            balance.value += float(request.form.get('value'))
        db.session.add(balance)
        db.session.commit()
    response = BalanceSchema().dump(Balance.query.filter_by(user_id=user_id).first())
    return Response(json.dumps(response), mimetype='application/json')


@app.route("/bank_account/statement/", methods=["GET"])
@token_required
@statement_counter
def statement(user_id):
    response = {}
    response.update({
        "credits": CreditSchema(many=True).dump(Credit.query.filter_by(user_id=user_id)),
        "debits": DebitSchema(many=True).dump(Debit.query.filter_by(user_id=user_id))
    })
    return Response(json.dumps(response), mimetype='application/json')
