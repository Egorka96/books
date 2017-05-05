from django.contrib.auth.models import User
from django.test import TestCase
from django.http import HttpResponse


class UserTestCase(TestCase):
    username = 'user'
    password = '123456qw'

    url = '/'

    def get_url(self):
        return self.url

    def generate_data(self):
        self.user = User.objects.create(username=self.username, password=self.password)

    def setUp(self):
        self.generate_data()

    def test_anonymous_user(self):
        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, 302)

    def test_authorized_user(self):
        self.client.force_login(self.user)
        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, 200)
