import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "")
    CELERY_BROKER_URL = 'redis://redis-svc:6379',
    CELERY_RESULT_BACKEND = 'redis://redis-svc:6379'