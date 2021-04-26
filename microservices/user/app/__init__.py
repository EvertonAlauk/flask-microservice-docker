import logging

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
app.config.from_object("app.config.Config")

db = SQLAlchemy(app)
metrics = PrometheusMetrics(app, group_by='path')

gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)

from app.models import *
from app.schemas import *
from app.views import *
from app.app_celery import celery
