from django.contrib.auth.models import User
from django.test import TestCase


class UserTestCase(TestCase):
    username = 'user'
    password = '123456qw'

    url = '/'
    protected_url = '/edit/1'

    def get_url(self):
        return self.url

    def get_protected_url(self):
        return self.protected_url

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

    def test_protected_view_with_permission(self):
        self.client.force_login(self.user)
        self.client.user_permisson.add('core.book.can_change_book')
        response = self.client.get(self.get_protected_url())
        self.assertEqual(response.status_code, 200)

    def test_protected_view_without_permission(self):
        self.client.force_login(self.user)
        response = self.client.get(self.get_protected_url())
        self.assertEqual(response.status_code, 302)
