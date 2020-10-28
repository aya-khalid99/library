import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Book, Techer


class LibraryTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "library_test"
        self.database_path = "postgres://{}:{}@{}/{}".format('postgres','1999','localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
    
    def tearDown(self):

        pass

    def test_get_paginated_books(self):
        res = self.client().get('/books')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
    
    def test_404_sent_requesting_beyond_valid_books(self):
        res = self.client().get('/books?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_get_paginated_techers(self):
        res = self.client().get('/techers')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['techers']))
    
    def test_404_sent_requesting_beyond_valid_techers(self):
        res = self.client().get('/techers?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

    def test_create_book(self):
        res = self.client().post('/books')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['books']))

    def test_400_for_failed_create_book(self):
        res = self.client().post('/books/45')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_create_techer(self):
        res = self.client().post('/techers')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['techers']))

    def test_400_for_failed_create_techer(self):
        res = self.client().post('/techers/45')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

    def test_delete_book(self):
        res = self.client().delete('/books/1')
        data = json.loads(res.data)
        book = Book.query.filter(Book.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertTrue(len(data['books']))
        self.assertEqual(book, None)

    def test_422_if_books_dose_not_exist(self):
        res = self.client().delete('/books/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_delete_techer(self):
        res = self.client().delete('/techers/1')
        data = json.loads(res.data)
        techer = Techer.query.filter(Techer.id == 1).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 1)
        self.assertTrue(len(data['techers']))
        self.assertEqual(techer, None)

    def test_422_if_techers_dose_not_exist(self):
        res = self.client().delete('/techers/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

    def test_get_book_search_with_results(self):
        res = self.client().post('/books', json={'search': 'Novel'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['books']))

    def test_get_book_search_without_results(self):
        res = self.client().post('/books', json={'search': 'canbe'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['books']), 0)

    def test_get_techer_search_with_results(self):
        res = self.client().post('/techers', json={'search': 'Novel'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['techers']))

    def test_get_techer_search_without_results(self):
        res = self.client().post('/techers', json={'search': 'canbe'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['techers']), 0)

    def test_update_techer(self):
        res = self.client().post('/techers/<int:techer_id>')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])
        self.assertTrue(len(data['techers']))

    def test_400_for_failed_updaTE_techer(self):
        res = self.client().post('/techers/<int:techer_id>/techer')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'bad request')

if __name__ == "__main__":
    unittest.main()

