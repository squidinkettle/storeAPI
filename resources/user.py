import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegistration(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
    type = str,
    required = True,
    help = "Please fill the required field")

    parser.add_argument('password',
    type = str,
    required = True,
    help = "Please fill the required field")

    def post(self):
        data = UserRegistration.parser.parse_args()
        if UserModel.find_by_user(data['username']):
            return {"Message":"That name is already taken"},400

        user = UserModel(**data)
        user.add_user()
        return {'message':'User created succesfully'},201
