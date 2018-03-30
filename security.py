from werkzeug.security import safe_str_cmp #if using python 2.7, it helps avoid unicoding problems
from models.user import UserModel

def authenticate(username,password):
    user = UserModel.find_by_user(username)
    if user and safe_str_cmp(user.password,password):
        return user

def identity(payload):
    user_id= payload['identity']
    return UserModel.find_by_id(user_id)



'''import datetime
app.config['JWT_EXPIRATION_DELTA'] = datetime.timedelta(seconds=1000)'''
#modify expiration time for JWT token
