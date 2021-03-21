from marshmallow import Schema
from marshmallow import fields


class CreditSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    value = fields.Float()


class DebitSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    value = fields.Float()

class BalanceSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    value = fields.Float()

