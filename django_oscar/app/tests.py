from django.test import Client, TestCase


class MyTestCase(TestCase):
    def setUp(self):
        self.client = Client()


class TestOpenPages(MyTestCase):
    def test_open_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
