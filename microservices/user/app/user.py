from werkzeug.security import generate_password_hash

class UserData:
    def __init__(self, username, email, password, name):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.name = name
