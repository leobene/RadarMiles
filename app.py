from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt import JWT, JWTError, current_identity
from security import authenticate, identity
from resources.user import UserRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'RadarMiles'
api = Api(app)


jwt = JWT(app, authenticate, identity)


api.add_resource(UserRegister, '/register')

@app.errorhandler(JWTError)
def auth_error(err):
    return jsonify({'message': 'Could not authorize. Did you include a valid Authorization header?'}), 401

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    @app.before_first_request
    def create_tables():
        db.create_all()

    app.run(port=5000, debug=True)
