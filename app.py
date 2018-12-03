from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager
from resources.user import UserRegister, User, UserLogin
from resources.company import Company, CompanyList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'RadarMiles'
#app.config['JWT_SECRET_KEY'] =
api = Api(app)


jwt = JWTManager(app)


api.add_resource(UserRegister, '/register')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(Company, '/company/<string:name>')
api.add_resource(CompanyList, '/companys')
api.add_resource(UserLogin, '/login')

#@app.errorhandler(JWTError)
#def auth_error(err):
 #   return jsonify({'message': 'Could not authorize. Did you include a valid Authorization header?'}), 401

if __name__ == '__main__':
    from db import db

    db.init_app(app)
    @app.before_first_request
    def create_tables():
        db.create_all()

    app.run(port=5000, debug=True)
