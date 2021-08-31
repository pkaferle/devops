# run with: python -m unittest test_connection.py
# Built-in unit test library
import unittest
# The module you want to test
import views_solutions


class TestConnection(unittest.TestCase):

    def test_settings(self):
        host = views_solutions.DB_HOST
        port = views_solutions.DB_PORT
        db = views_solutions.DB_NO
        self.assertEqual(host, 'localhost')
        self.assertEqual(port, 6379)
        self.assertEqual(db, 1)
