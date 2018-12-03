from flask_restful import Resource
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
    def get(self):
        return {'Companhias': [company.json() for company in CompanyModel.find_all()]}

