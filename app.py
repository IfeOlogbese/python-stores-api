from flask import Flask
from flask_restful import Api
from flask_jwt import JWT  # import JWT
from security import authenticate, identity
# from db.database import Database
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.secret_key = "some secret key"
api = Api(app)  # Allow us to very easily add http resources

""" Api works with resources and every resource has to be a class"""

# creates new endpoint /auth, we send username and password, JWT gets it and sends to the authenticate method
jwt = JWT(app, authenticate, identity)

# @app.before_first_request # initialize database connection
# def init_db():
#     Database.initialize()


api.add_resource(Item, '/item/<string:name>')  # http://localhost:5000/item/ife
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # debug to true for proper error messages
