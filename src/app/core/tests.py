# -*- coding: utf-8 -*-

from model_mommy import mommy
from django.test import TestCase
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse_lazy
from app.fleet.models import Fleet
from app.core.utils import CPF
from app.core import views


class CpfTest(TestCase):

    def setUp(self):
        self.cpf_with_formatting = CPF('010.787.400-89')
        self.cpf_without_formatting = CPF('01078740089')

    def test_cpf_with_formatting_validate_suze_return_true(self):
        self.assertTrue(self.cpf_with_formatting.validate_size())

    def test_cpf_without_formatting_validate_suze_return_true(self):
        self.assertTrue(self.cpf_without_formatting.validate_size())

    def test_cpf_validate_size_return_false(self):
        cpf = CPF('1234567891')
        self.assertFalse(cpf.validate_size())

    def test_cpf_format_return_true(self):
        self.assertEqual(self.cpf_without_formatting.format(), '010.787.400-89')

    def test_cpf_format_return_false(self):
        self.assertNotEqual(self.cpf_without_formatting.format(), '01078740089')

    def test_cpf_cleaning_return_true(self):
        self.assertEqual(self.cpf_with_formatting.cleaning(), '01078740089')

    def test_cpf_cleaning_return_false(self):
        self.assertNotEqual(self.cpf_with_formatting.cleaning(),
            '010787400-89')

    def test_cpf_with_formatting_validate_return_true(self):
        self.assertTrue(self.cpf_with_formatting.validate())

    def test_cpf_with_formatting_validate_return_false(self):
        cpf = CPF('010.787.400-8')
        self.assertFalse(cpf.validate())

    def test_cpf_without_formatting_validate_return_false(self):
        cpf = CPF('0107874008')
        self.assertFalse(cpf.validate())

    def test_cpf_without_formatting_validate_return_true(self):
        self.assertTrue(self.cpf_without_formatting.validate())


class ViewsTestCase(TestCase):

    def setUp(self):
        mommy.make(Fleet, _quantity=5)

    def test_page_403(self):
        request = RequestFactory()
        response = views.page_403(request)

        self.assertEqual(response.status_code, 403)

    def test_home(self):
        response = self.client.get(reverse_lazy('index'))

        self.assertEqual(response.context['object_list'].count(), 5)
