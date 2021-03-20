import random
import string
import os

basedir = os.path.abspath(os.path.dirname(__file__))
random_str = string.ascii_letters + string.digits + string.ascii_uppercase

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ''.join(random.choice(random_str) for i in range(12))