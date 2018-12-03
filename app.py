from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from blacklist import BLACKLIST
from resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh
from resources.company import Company, CompanyList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True  # enable blacklist feature
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']  # allow blacklisting for access and refresh tokens
app.secret_key = 'RadarMiles'
#app.config['JWT_SECRET_KEY'] =
api = Api(app)


jwt = JWTManager(app)


api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(Company, '/company/<string:name>')
api.add_resource(CompanyList, '/companys')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(TokenRefresh, '/refresh')

#@app.errorhandler(JWTError)
#def auth_error(err):
 #   return jsonify({'message': 'Could not authorize. Did you include a valid Authorization header?'}), 401

# This method will check if a token is blacklisted, and will be called automatically when blacklist is enabled
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST

# The following callbacks are used for customizing jwt response/error messages.
@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'description': 'The token has expired.',
        'error': 'token_expired'
    }), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'description': 'Signature verification failed.',
        'error': 'invalid_token'
    }), 401


@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'description': 'Request does not contain an access token.',
        'error': 'authorization_required'
    }), 401


@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({
        'description': 'The token is not fresh.',
        'error': 'fresh_token_required'
    }), 401


@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        'description': 'The token has been revoked.',
        'error': 'token_revoked'
    }), 401

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    @app.before_first_request
    def create_tables():
        db.create_all()

    app.run(port=5000, debug=True)
