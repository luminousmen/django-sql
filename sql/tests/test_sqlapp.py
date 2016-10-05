# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase, RequestFactory, Client
from django.contrib.admin.sites import AdminSite
from django.core.urlresolvers import reverse

from ..admin import SQLAdmin
from ..sqlapp import execute_sql


class AdminTests(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='test',
            email='test@test.com',
            password='top_secret',
            is_staff=True
        )
        self.client = Client()
        self.client.login(username='test', password='top_secret')

    def test_getting_view(self):
        response = self.client.get(reverse('sql'), {
            'user_id': self.user.id
        }, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_execeuting_valid_sql(self):
        response = self.client.post(reverse('sql'), {
            'user_id': self.user.id,
            'query': "select * from auth_user"
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("<p>Rows: 1</p>" in str(response.content))

    def test_execeuting_sql_with_no_tables(self):
        response = self.client.post(reverse('sql'), {
            'user_id': self.user.id,
            'query': "select *"
        }, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue("<pre>no tables specified</pre>" in str(response.content))
