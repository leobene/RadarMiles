from models.company import CompanyModel
from tests.base_test import BaseTest
import json


class CompanyTest(BaseTest):
    def test_company_not_found(self):
        with self.app() as c:
            r = c.get('/company/test')
            self.assertEqual(r.status_code, 404)

    def test_company_found(self):
        with self.app() as c:
            with self.app_context():
                CompanyModel('Azul').save_to_db()
                r = c.get('/company/Azul')

                self.assertEqual(r.status_code, 200)
                self.assertDictEqual(d1={'company': {'id': 1, 'name': 'Azul'}},
                                     d2=json.loads(r.data.decode('utf-8')))

    def test_delete_company(self):
        with self.app() as c:
            with self.app_context():
                CompanyModel('Azul').save_to_db()
                r = c.delete('/company/Azul')

                self.assertEqual(r.status_code, 200)
                self.assertDictEqual(d1={'message': 'Company deleted'},
                                     d2=json.loads(r.data.decode('utf-8')))

    def test_create_company(self):
        with self.app() as c:
            with self.app_context():
                r = c.post('/company/Azul')

                self.assertEqual(r.status_code, 201)
                self.assertIsNotNone(CompanyModel.find_by_name('Azul'))
                self.assertDictEqual(d1={'id': 1, 'name': 'Azul'},
                                     d2=json.loads(r.data.decode('utf-8')))

    def test_create_duplicate_company(self):
        with self.app() as c:
            with self.app_context():
                c.post('/company/Azul')
                r = c.post('/company/Azul')

                self.assertEqual(r.status_code, 500)
                self.assertDictEqual(d1={'message': "An company with name '{}' already exists.".format('Azul')},
                                     d2=json.loads(r.data.decode('utf-8')))
