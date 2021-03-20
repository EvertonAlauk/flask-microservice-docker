from marshmallow import Schema
from marshmallow import fields

class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Str()
    name = fields.Str()
    active = fields.Bool()
    created = fields.DateTime()
