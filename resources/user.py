import sqlite3
from flask_restful import Resource, reqparse
from Code.models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help='This field cannot left blank'
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help='This field cannot left blank'
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"Message": "This User is Already exists"}, 400
        user = UserModel(**data)
        user.save_to_db()
        return {'Message': '{} Has Been Created Successfully'.format(data['username'])}, 201


class UserList(Resource):
    def get(self):
        data = UserRegister.parser.parse_args()
        return UserModel.query.filter_by(username=data['username']).first()
