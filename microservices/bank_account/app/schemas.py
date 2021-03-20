from marshmallow import Schema
from marshmallow import fields


class CreditSchema(Schema):
    id = fields.Int()
    user_id = fields.Int()
    credit = fields.Float()

