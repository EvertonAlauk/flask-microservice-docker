from enum import Enum

class AuthExceptions(Enum):
    ERROR = {"error": "Error in bank account API: {}"}
    JWT_NOT_FOUND = {"error": "Token is missing."}
