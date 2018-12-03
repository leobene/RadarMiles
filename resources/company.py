from flask_restful import Resource
from flask_jwt_extended import jwt_required, jwt_optional, get_jwt_identity
from models.company import CompanyModel


class Company(Resource):
    def get(self, name):
        company = CompanyModel.find_by_name(name).first()
        if company:
            return {'company': company.json()}
        return {'message': 'Company not found'}, 404

    def post(self, name):
        if CompanyModel.find_by_name(name).first():
            return {'message': "An company with name '{}' already exists.".format(name)}, 500

        company = CompanyModel(name)
        try:
            company.save_to_db()
        except:
            return {"message": "An error occurred inserting the company."}, 500

        return company.json(), 201

    #@jwt_required
    def delete(self, name):
        company = CompanyModel.find_by_name(name).first()
        if company:
            company.delete_from_db()

        return {'message': 'Company deleted'}, 200


class CompanyList(Resource):
    @jwt_optional
    def get(self):
        user_id = get_jwt_identity()
        companys = [company.json() for company in CompanyModel.find_all()]
        if user_id:
            return {'Companhias': companys}, 200

        return {
            'Companhias': [company['name'] for company in companys],
            'Message': 'More data available if you log in'
        }

