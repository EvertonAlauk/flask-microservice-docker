import datetime

from app import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(60), nullable=False)
    active = db.Column(db.Boolean(), default=True, nullable=False)
    created = db.Column(db.DateTime(), default=datetime.datetime.now())

    def __init__(self, username, email, password, name):
        self.username = username
        self.email = email
        self.password = password
        self.name = name
