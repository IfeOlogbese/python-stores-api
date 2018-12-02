from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager  # import JWT
from resources.user import UserRegister, User, UserLogin, TokenRefresh
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True  # for proper Flask JWT errors
app.secret_key = "some secret key"  # app.config['JWT_SECRET_KEY]
api = Api(app)  # Allow us to very easily add http resources

""" Api works with resources and every resource has to be a class"""

jwt = JWTManager(app)


@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity: #do something here instead of hardcoding this
        return {'is_admin': True}
    return {'is_admin': False}

# call backs
@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'description': 'The token has expired',
        'error': 'token_expired'
    }), 401

# When token that was sent isn't valid
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'description': 'Signature verification failed.',
        'error': 'invalid_token'
    }), 401

# When no token was sent at all
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'description': 'Request does not contain an access token.',
        'error': 'invalid_token'
    }), 401

# When no fresh token was sent
@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({
        'description': 'The token is not fresh.',
        'error': 'fresh_token_required'
    }), 401

# When no fresh token was sent
@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        'description': 'The token has been revoked.',
        'error': 'token_revoked'
    }), 401

api.add_resource(Item, '/item/<string:name>')  # http://localhost:5000/item/ife
api.add_resource(ItemList, '/items')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<string:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(TokenRefresh, '/refresh')

if __name__ == '__main__':
    app.run(port=5000, debug=True)  # debug to true for proper error messages
