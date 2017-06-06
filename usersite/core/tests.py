from django.contrib.auth.models import User, Permission
from django.test import TestCase
from django.urls import reverse_lazy, reverse

from core import models


class UserTestCase(TestCase):
    username = 'user'
    password = '123456qw'

    def get_url(self):
        return reverse('edit', kwargs={'pk': self.book.id})

    def generate_data(self):
        self.user = User.objects.create(username=self.username, password=self.password)
        self.author = models.Author.objects.create(name='test_author', contacts='some')
        self.book = models.Book.objects.create(author=self.author, title='some title', pub_date='2015-02-02')

    def setUp(self):
        self.generate_data()

    def test_anonymous_user(self):
        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, 302)

    def test_user_with_permission(self):
        permission = Permission.objects.get(codename='change_book')
        self.user.user_permissions.add(permission)
        self.client.force_login(self.user)
        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, 200)

    def test_user_without_permission(self):
        self.client.force_login(self.user)
        response = self.client.get(self.get_url())
        self.assertEqual(response.status_code, 302)
