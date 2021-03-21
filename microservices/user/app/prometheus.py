from flask import request

from app import metrics

user_counter = metrics.counter(
    'user_counter', 'API user metrics',
    labels={'path': lambda: request.path}
)

auth_counter = metrics.counter(
    'auth_counter', 'API auth metrics',
    labels={'path': lambda: request.path}
)