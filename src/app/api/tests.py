# -*- coding: utf-8 -*-

import json
from base64 import b64encode
from rest_framework import exceptions
from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import AnonymousUser
from app.core.test_helpers import Helper
from app.api.auth import Authenticate

class AuthTestCase(Helper, TestCase):

    def setUp(self):
        super(AuthTestCase, self).setUp()
        self.auth = Authenticate()

    def test_get_path(self):
        request = self.factory.get(reverse_lazy('api-v1:customer-detail',
            args=[self.customer.id]), **self.headers)

        self.assertEqual(self.auth._get_path(request), 'customer-detail')

    def test_allowed_path(self):
        data = {
            "first_name": "Adriano",
            "last_name": "Margarin",
            "username": "adrianomargarin",
            "email": "adriano.margarin@gmail.com",
            "cpf": "01078740089",
            "cnh_type": ["A", "B"],
            "password": "123456"
        }
        request = self.factory.post(reverse_lazy('api-v1:customer-list'),
            data=data, **self.headers)

        self.assertTrue(self.auth._allowed_path(request))

    def test_bad_credentials(self):
        self.assertRaises(exceptions.AuthenticationFailed,
            self.auth.bad_credentials)

    def test_get_authorization_header(self):
        request = self.factory.get(reverse_lazy('api-v1:customer-detail',
            args=[self.customer.id]), **self.headers)
        auth = self.auth.get_authorization_header(request)

        self.assertEqual(auth, 'Basic Y2xpZW50ZTpjbGllbnRl')

    def test_get_authorization_header_not_header(self):
        request = self.factory.get(reverse_lazy('api-v1:customer-detail',
            args=[self.customer.id]))
        auth = self.auth.get_authorization_header(request)

        self.assertEqual(auth, '')

    def test_authenticate_credentials_anonymous_user(self):
        self.assertTrue(isinstance(self.auth.authenticate_credentials(
            anonymous=True)[0], AnonymousUser))

    def test_authenticate_credentials(self):
        request = self.factory.get(reverse_lazy('api-v1:customer-detail',
            args=[self.customer.id]), **self.headers)
        auth = self.auth.authenticate_credentials(request=request,
            username=self.customer.username, password='cliente')

        self.assertEqual(auth[0].username, self.customer.username)

    def test_authenticate_credentials_raise(self):
        request = self.factory.get(reverse_lazy('api-v1:customer-detail',
            args=[self.customer.id]), **self.headers)

        def raises():
            self.auth.authenticate_credentials(request=request,
                username=self.customer.username, password='errado')

        self.assertRaises(exceptions.AuthenticationFailed, raises)

    def test_authenticate_credentials_not_admin(self):
        request = self.factory.get(reverse_lazy('api-v1:fleet-detail',
            args=[self.vehicle.id]), **self.headers)

        def raises():
            self.auth.authenticate_credentials(request=request,
                username=self.customer.username, password='cliente')

        self.assertRaises(exceptions.AuthenticationFailed, raises)

    def test_authenticate_credentials_admin(self):
        user_pass = b64encode(
            self.superuser.username + ':' + 'admin').decode('ascii')
        self.headers = {'HTTP_AUTHORIZATION': 'Basic %s' % user_pass}

        request = self.factory.get(reverse_lazy('api-v1:fleet-detail',
            args=[self.vehicle.id]), **self.headers)

        auth = self.auth.authenticate_credentials(request=request,
            username=self.superuser.username, password='admin')

        self.assertEqual(auth[0].username, self.superuser.username)


    def test_authenticate_credentials_does_not_exist(self):
        user_pass = b64encode(
            self.superuser.username + ':' + 'admin').decode('ascii')
        self.headers = {'HTTP_AUTHORIZATION': 'Basic %s' % user_pass}

        request = self.factory.get(reverse_lazy('api-v1:fleet-detail',
            args=[self.vehicle.id]), **self.headers)

        def raises():
            self.auth.authenticate_credentials(request=request,
                username='inexistente', password='admin')

        self.assertRaises(exceptions.AuthenticationFailed, raises)

    def test_authenticate_anonymous_user(self):
        request = self.factory.post(reverse_lazy('api-v1:customer-list'),
            data={})

        auth = self.auth.authenticate(request)
        self.assertTrue(isinstance(auth[0], AnonymousUser))

    def test_authenticate_bad_credentials(self):
        self.headers = {'HTTP_AUTHORIZATION': 'Basic %s' % ''}

        request = self.factory.get(reverse_lazy('api-v1:fleet-detail',
            args=[self.vehicle.id]), **self.headers)

        def raises():
            self.auth.authenticate(request)

        self.assertRaises(exceptions.AuthenticationFailed, raises)

    def test_authenticate(self):
        user_pass = b64encode(
            self.superuser.username + ':' + 'admin').decode('ascii')
        self.headers = {'HTTP_AUTHORIZATION': 'Basic %s' % user_pass}
        request = self.factory.get(reverse_lazy('api-v1:fleet-detail',
            args=[self.vehicle.id]), **self.headers)

        auth = self.auth.authenticate(request)

        self.assertEqual(auth[0], self.superuser)
