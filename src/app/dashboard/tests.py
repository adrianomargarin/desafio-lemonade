# -*- coding: utf-8 -*-

from model_mommy import mommy
from django.test import TestCase
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse_lazy
from app.customer.models import Customer
from app.dashboard import views
from app.rentacar import models
from app.core.test_helpers import Helper

class ViewsTestCase(Helper, TestCase):

    def setUp(self):
        super(ViewsTestCase, self).setUp()

    def test_queryset(self):
        self.login()
        response = self.client.get(reverse_lazy('dashboard:rent'))

        self.assertEqual(response.context['object_list'].count(), 1)
