from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, id, username, password, active):
        self.id = id
        self.username = username
        self.password = password
        self.active = active

    def is_authenticated(self):
        return True

    def is_active(self):
        return self.active

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return f'<User {self.username}>'
