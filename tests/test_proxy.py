from unittest import TestCase
from app import Proxy


class TestProxy(TestCase):
    def test_proxy(self):
        response = Proxy.get('/google')
        self.assertEqual(response.status_code, 200)
