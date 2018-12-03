from models.company import CompanyModel
from tests.base_test import BaseTest


class CompanyTest(BaseTest):
    def test_crud(self):
        with self.app_context():
            competition = CompanyModel('GOL')

            self.assertIsNone(CompanyModel.find_by_name('GOL'), "Found an competition with name 'GOL' before save_to_db")

            competition.save_to_db()

            self.assertIsNotNone(CompanyModel.find_by_name('GOL'),
                                 "Did not find a competition with name 'GOL' after save_to_db")

            competition.delete_from_db()

            self.assertIsNone(CompanyModel.find_by_name('GOL'), "Found an competition with name 'GOL' after delete_from_db")

