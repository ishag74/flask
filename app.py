from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from Code.security import identity, authenticate
from Code.resources.user import UserRegister, UserList
from Code.resources.item import Item, ItemList
from Code.resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # this is flask extension for modification in the db (SQLALCHEMY has its own tracker)
app.secret_key = 'isaac'
api = Api(app)


jwt = JWT(app, authenticate, identity)  # when initialize it creates endpoint called /auth

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/item')
api.add_resource(UserRegister, '/register')
api.add_resource(UserList, '/users')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
