from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp


class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

#temp usertest
users = [
    User(1, 'user1', '123'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def is_authenticate(username, password):
    ''' TEMP ''' 
    global users
    for user in users:
        if user.username == username and user.password == password:
            return True
    return False

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)
