from enum import Enum

class UserExceptions(Enum):
    ERROR = {"error": "Error in user API: {}"}

class AuthExceptions(Enum):
    ERROR = {"error": "Error in user API: {}"}
    USER_NOT_FOUND = {"error": "User not found."}
    AUTH_NOT_FOUND = {"error": "Auth not found."}
    PASSWORD_NOT_MATCH = {"error": "Password not match."}