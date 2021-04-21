from enum import Enum

class AuthExceptions(Enum):
    ERROR = "Error in bank account API: {}"
    JWT_NOT_FOUND = "Token is missing."

class BankAccountExceptions(Enum):
    VALUE_EMPTY = "Value empty."
    BALANCE_EMPTY = "Balance empty."

