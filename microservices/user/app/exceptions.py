from enum import Enum

class UserExceptions(Enum):
    ERROR = "Error in user API: {}"
    USER_ID_IS_MISSING = "Parameter *user_id* is missing."
    USER_ID_NOT_FOUND = "User with parameter *{}* is not found."

class AuthExceptions(Enum):
    ERROR = {"error": "Error in user API: {}"}
    USER_NOT_FOUND = {"error": "User not found."}
    AUTH_NOT_FOUND = {"error": "Auth not found."}
    PASSWORD_NOT_MATCH = {"error": "Password not match."}