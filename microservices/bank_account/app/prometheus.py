from flask import request

from app import metrics

balance_counter = metrics.counter(
    'balance_counter', 'API balance metrics',
    labels={'path': lambda: request.path}
)

credit_counter = metrics.counter(
    'credit_counter', 'API credit metrics',
    labels={'path': lambda: request.path}
)

debit_counter = metrics.counter(
    'debit_counter', 'API debit metrics',
    labels={'path': lambda: request.path}
)

statement_counter = metrics.counter(
    'statement_counter', 'API statement metrics',
    labels={'path': lambda: request.path}
)