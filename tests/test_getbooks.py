import unittest

from api import app

class GetBooksTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_successful_getbooks(self):

        response = self.app.get('/books', headers={"Content-Type": "application/json"})
        self.assertEqual(200, response.status_code)

    def test_successful_getbookssize(self):

        response = self.app.get('/books', headers={"Content-Type": "application/json"})
        self.assertEqual(3, len(response.json['books']))


