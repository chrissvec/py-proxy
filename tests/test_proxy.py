from unittest import TestCase
from app import Proxy


class TestProxy(TestCase):
    def test_proxy(self):
        response = Proxy.get('/google')
        self.assertEqual(response.status_code, 200)

    def test_health(self):
        response = Proxy.get('/healthcheck')
        self.assertEqual(response.status_code, 200)

    def test_null(self):
        response = Proxy.get('/')
        self.assertEqual(response.status_code, 200)
