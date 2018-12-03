from models.company import CompanyModel
from tests.base_test import BaseTest


class CompanyTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            competition = CompanyModel('AVIANCA')

            self.assertIsNone(CompanyModel.find_by_name('AVIANCA').first(), "Found an competition with name 'AVIANCA' before save_to_db")

            competition.save_to_db()

            self.assertIsNotNone(CompanyModel.find_by_name('AVIANCA').first(),
                                 "Did not find a competition with name 'AVIANCA' after save_to_db")

            competition.delete_from_db()

            self.assertIsNone(CompanyModel.find_by_name('AVIANCA').first(), "Found an competition with name 'AVIANCA' after delete_from_db")

