from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("app.config.Config")
db = SQLAlchemy(app)

with app.app_context():
    from app.models import *
    from app.schemas import *
    from app.views import *
