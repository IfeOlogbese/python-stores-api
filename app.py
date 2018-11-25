from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager  # import JWT
from resources.user import UserRegister, User, UserLogin
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True # for proper Flask JWT errors
app.secret_key = "some secret key" # app.config['JWT_SECRET_KEY]
api = Api(app)  # Allow us to very easily add http resources

""" Api works with resources and every resource has to be a class"""

jwt = JWTManager(app)

api.add_resource(Item, '/item/<string:name>')  # http://localhost:5000/item/ife
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<string:user_id>')
api.add_resource(UserLogin, '/login')

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # debug to true for proper error messages
