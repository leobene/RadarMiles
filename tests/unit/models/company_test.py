from models.company import CompanyModel
from tests.base_test import BaseTest


class CompetitionTest(BaseTest):
    def test_create_competition(self):
        company = CompanyModel('GOL')

        self.assertEqual(company.name, 'GOL',
                         "The name of the company after creation does not equal the constructor argument.")

    def test_competition_json(self):
        company = CompanyModel('GOL')
        expected = {
            'id': company.id,
            'name': company.name,
        }

        self.assertEqual(
            company.json(),
            expected,
            "The JSON export of the company is incorrect. Received {}, expected {}.".format(company.json(), expected))
