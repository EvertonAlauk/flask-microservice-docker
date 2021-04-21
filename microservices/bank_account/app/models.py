import datetime

from app import db

class Credit(db.Model):
    __tablename__ = "credits"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer())
    value = db.Column(db.Float(precision=8, asdecimal=False))
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created = db.Column(db.DateTime(), default=datetime.datetime.now())

    def __init__(self, user_id, value):
        self.user_id = user_id
        self.value = value

    def create(self):
        db.session.add(self)
        db.session.commit()


class Debit(db.Model):
    __tablename__ = "debits"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer())
    value = db.Column(db.Float(precision=8, asdecimal=False))
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created = db.Column(db.DateTime(), default=datetime.datetime.now())

    def __init__(self, user_id, value):
        self.user_id = user_id
        self.value = value

    def create(self):
        db.session.add(self)
        db.session.commit()


class Balance(db.Model):
    __tablename__ = "balances"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer())
    value = db.Column(db.Float(precision=8, asdecimal=False))
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created = db.Column(db.DateTime(), default=datetime.datetime.now())

    def __init__(self, user_id, value):
        self.user_id = user_id
        self.value = value

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def credit(self, value):
        if not self.value:
            return self
        self.value = self.value + float(value)
        db.session.add(self)
        db.session.commit()
        return self

    def debit(self, value):
        if not self.value:
            return self
        self.value = self.value - float(value)
        db.session.add(self)
        db.session.commit()
        return self
