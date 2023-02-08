import unittest
import requests

class TestAPI(unittest.TestCase):
    def test_users(self):
        response = requests.get('http://localhost:5000/api/users?since=1')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.text) > 0)

    def test_user_details(self):
        response = requests.get('http://localhost:5000/api/users/BrunoSoaresV/details')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.text) > 0)

    def test_user_repos(self):
        response = requests.get('http://localhost:5000/api/users/BrunoSoaresV/repos')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.text) > 0)

if __name__ == '__main__':
    unittest.main()