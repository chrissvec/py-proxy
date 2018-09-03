import unittest
from app import spawn_proxy


class TestProxy(unittest.TestCase):
    def setUp(self):
        self.app = spawn_proxy()
        self.client = self.app.test_client

    def tearDown(self):
        pass

    def test_proxy(self):
        response = self.client().get('/bose')
        self.assertEqual(response.status_code, 200)

    def test_health(self):
        response = self.client().get('/healthcheck')
        self.assertEqual(response.status_code, 200)

    def test_null(self):
        response = self.client().get('/')
        self.assertEqual(response.status_code, 400)


if __name__ == "__main__":
    unittest.main()
