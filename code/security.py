from werkzeug.security import safe_str_cmp # for comparing strings
from models.user import UserModel

# authenticate method to be run by JWT in authenticating a user
def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user

# this is the function to identify user from the token
def identity(payload):
    user_id = UserModel.find_by_id(payload['identity'])
    return user_id
