# -*- coding: utf-8 -*-

import base64

from django.core.urlresolvers import resolve
from django.contrib.auth.models import AnonymousUser

from rest_framework import exceptions
from rest_framework import authentication
from rest_framework.permissions import BasePermission

from django.contrib.auth.models import User

ALLOWED_PATHS = [
    'customer-list',
]

ALLOWED_PATHS_ADMIN = [
    'fleet-list',
    'fleet-detail'
]

class Authenticate(authentication.BasicAuthentication):
    """
    Custom auth method to authenticate the user trought the token
    """

    def _get_path(self, request):
        return resolve(request.path).url_name

    def _allowed_path(self, request):
        url_name = self._get_path(request)
        return True if url_name in ALLOWED_PATHS else False

    def _allowed_path_admin(self, request):
        url_name = self._get_path(request)
        return True if url_name in ALLOWED_PATHS_ADMIN else False

    def bad_credentials(self):
        raise exceptions.AuthenticationFailed('Bad credentials')

    def get_authorization_header(self, request):
        auth = request.META.get('HTTP_AUTHORIZATION', b'')
        if type(auth) == type(''):
            auth = auth.encode('iso-8859-1')

        return auth

    def authenticate_credentials(self, username=None, password=None,
        anonymous=False, request=None):

        if anonymous:
            return (AnonymousUser(), None)


        try:
            user = User.objects.get(username=username)

            if not user.check_password(password):
                self.bad_credentials()

            if self._allowed_path_admin(request) and not user.is_superuser:
                self.bad_credentials()

        except User.DoesNotExist:
            self.bad_credentials()

        return (user, None)

    def authenticate(self, request, simple=False):
        auth = self.get_authorization_header(request).split()

        if not auth and self._allowed_path(request) or self._allowed_path(request):
            return self.authenticate_credentials(anonymous=True)

        try:
            auth_parts = base64.b64decode(auth[1]).decode('iso-8859-1').partition(':')
        except (IndexError, TypeError):
            self.bad_credentials()

        username, password = auth_parts[0], auth_parts[2]

        return self.authenticate_credentials(username, password, request=request)
