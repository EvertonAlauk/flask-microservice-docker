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


@app.route("/bank_account/balance/", methods=["GET", "POST"])
@token_required
@balance_counter
def balance(user_id):
    balance = Balance.query.filter_by(user_id=user_id).first()
    if request.method == "POST":
        value = request.json.get('value')
        if not balance:
            balance = Balance(user_id=user_id, value=value).create()
        else:
            balance.credit(value=value)
    return Response(json.dumps({
        "balance": BalanceSchema().dump(balance)
    }), mimetype='application/json')


@app.route("/bank_account/statement/", methods=["GET"])
@token_required
@statement_counter
def statement(user_id):
    credit = Credit.query.filter_by(user_id=user_id)
    debit = Debit.query.filter_by(user_id=user_id)
    balance = Balance.query.filter_by(user_id=user_id).first()
    return Response(json.dumps({
        "credits": CreditSchema(many=True).dump(credit),
        "debits": DebitSchema(many=True).dump(debit),
        "balance": BalanceSchema(many=False).dump(balance),
    }), mimetype='application/json')


@app.route("/bank_account/credit/", methods=["POST"])
@token_required
@credit_counter
def credit(user_id):
    if request.method == "POST":
        value = request.json.get('value')
        credit = Credit(user_id=user_id, value=value)
        credit.create()
        balance = Balance.query.filter_by(user_id=user_id).first()
        balance.credit(value=credit.value)
        return Response(json.dumps({
            "credit": CreditSchema().dump(credit),
            "balance": BalanceSchema().dump(balance),
        }), mimetype='application/json')


@app.route("/bank_account/debit/", methods=["POST"])
@token_required
@debit_counter
def debit(user_id):
    if request.method == "POST":
        value = request.json.get('value')
        debit = Debit(user_id=user_id, value=value)
        debit.create()
        balance = Balance.query.filter_by(user_id=user_id).first()
        balance.debit(value=debit.value)
        return Response(json.dumps({
            "debit": DebitSchema().dump(debit),
            "balance": BalanceSchema().dump(balance),
        }), mimetype='application/json')
