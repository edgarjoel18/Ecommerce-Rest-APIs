import sqlite3
from flask_restful import Resource, reqparse
from models.user import User


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username", type=str, required=True, help="username is required")
    parser.add_argument("password", type=str, required=True, help="password is required")

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {'message': 'A user with that username already exists'}, 400

        new_user = User(**data)
        new_user.save_to_db()
        return {'message': 'User created successfully'}, 201
        # if User.find_by_username(data['username']):
        #     return {'message': "A user with that username already exists"}, 400
        #
        # connection = sqlite3.connect("data.db")
        # cursor = connection.cursor()
        # query = "INSERT INTO users VALUES (NULL,?,?)"
        # cursor.execute(query, (data['username'], data['password']))
        #
        # connection.commit()
        # connection.close()
        # return {'message': "User created"}, 201
