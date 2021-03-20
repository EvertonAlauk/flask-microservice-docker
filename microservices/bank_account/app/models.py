import datetime

from app import db

class Credit(db.Model):
    __tablename__ = "credits"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer())
    credit = db.Column(db.Float(precision=8, asdecimal=False))
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created = db.Column(db.DateTime(), default=datetime.datetime.now())

    def __init__(self, user_id, credit):
        self.user_id = user_id
        self.credit = credit

