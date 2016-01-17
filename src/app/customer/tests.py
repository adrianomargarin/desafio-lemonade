# -*- coding: utf-8 -*-

from model_mommy import mommy
from django.test import TestCase
from django.forms import ValidationError
from django.core.urlresolvers import reverse_lazy
from app.customer import forms
from app.customer import models
from app.customer import views


class FormTestCase(TestCase):

    def setUp(self):
        self.data = {
            'first_name': u'Adriano',
            'last_name': u'Margarin',
            'username': u'adriano',
            'email': u'adriano.margarin@gmail.com',
            'cpf': u'01708132236',
            'cnh_type': [u'A', u'B'],
            'password': u'123',
            'password2': u'123'
        }

    def test_form_save(self):
        form = forms.CustomerForm(data=self.data)
        self.assertTrue(form.is_valid())

        customer = form.save()

        self.assertEqual(customer.first_name, self.data['first_name'])
        self.assertEqual(customer.last_name, self.data['last_name'])
        self.assertEqual(customer.username, self.data['username'])
        self.assertEqual(customer.email, self.data['email'])
        self.assertEqual(customer.cpf, self.data['cpf'])
        self.assertEqual(customer.cnh_type, self.data['cnh_type'])
        self.assertEqual(customer.password, self.data['password'])

    def test_form_clean(self):
        def error():
            self.data['password2'] = u'321'
            form = forms.CustomerForm(data=self.data)
            form.is_valid()

        self.assertRaises(ValidationError, error())


class ModelsTestCase(TestCase):

    def setUp(self):
        self.customer = mommy.make(models.Customer, cpf='01708132236')

    def test_format_cpf(self):
        self.assertEqual(self.customer.format_cpf(), '017.081.322-36')

    def test_unicode_full_name(self):
        self.customer.first_name = 'Adriano'
        self.customer.last_name = 'Margarin'
        self.customer.save()

        self.assertEqual(self.customer.__unicode__(), 'Adriano Margarin')

    def test_unicode_username(self):
        self.customer.username = 'adriano'
        self.customer.save()

        self.assertEqual(self.customer.__unicode__(), 'adriano')


class ViewsTestCase(TestCase):

    def setUp(self):
        self.data = {
            'first_name': u'Adriano',
            'last_name': u'Margarin',
            'username': u'adriano',
            'email': u'adriano.margarin@gmail.com',
            'cpf': u'01708132236',
            'cnh_type': [u'A', u'B'],
            'password': u'123',
            'password2': u'123'
        }

    def test_create_customer(self):
        response = self.client.post(reverse_lazy('customer:register'),
            data=self.data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, 'http://testserver/login')

        customer = models.Customer.objects.get(cpf=self.data['cpf'])

        self.assertEqual(customer.first_name, self.data['first_name'])
        self.assertEqual(customer.last_name, self.data['last_name'])
        self.assertEqual(customer.username, self.data['username'])
        self.assertEqual(customer.email, self.data['email'])
        self.assertEqual(customer.cpf, self.data['cpf'])
        self.assertEqual(customer.cnh_type, self.data['cnh_type'])


    def test_create_customer_with_invalid_cpf(self):
        self.data['cpf'] = '11111111111'
        response = self.client.post(reverse_lazy('customer:register'),
            data=self.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors['cpf'],
            [u'CPF inválido.'])

    def test_create_customer_with_duplicated_cpf(self):
        customer = mommy.make(models.Customer, cpf='01708132236')
        self.data['cpf'] = customer.cpf

        response = self.client.post(reverse_lazy('customer:register'),
            data=self.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors['cpf'],
            [u'Cliente com este CPF já existe.'])

    def test_create_customer_with_invalida_password(self):
        self.data['password2'] = '321'

        response = self.client.post(reverse_lazy('customer:register'),
            data=self.data)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['form'].errors['__all__'],
            [u'As senhas não conferem.'])
