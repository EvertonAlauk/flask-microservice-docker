from marshmallow import Schema, fields

class UserSchema(Schema):
    id = fields.Int()
    email = fields.Str()
    active = fields.Bool()
