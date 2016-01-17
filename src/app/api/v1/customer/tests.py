# -*- coding: utf-8 -*-

import json
from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from app.core.test_helpers import Helper


class CustomerTestCase(Helper, TestCase):

    def setUp(self):
        super(CustomerTestCase, self).setUp()

    def test_get_single_object(self):
        response = self.client.get(reverse_lazy('api-v1:customer-detail',
            args=[self.customer.id]), **self.headers)
        content = json.loads(response.content)

        self.assertEqual(content['id'], self.customer.id)

    def test_get_single_object_does_not_exist(self):
        response = self.client.get(reverse_lazy('api-v1:customer-detail',
            args=[999]), **self.headers)

        self.assertEqual(response.status_code, 404)

    def test_create(self):
        data = {
            'first_name': 'Adriano',
            'last_name': 'Margarin',
            'username': 'adrianomargarin',
            'email': 'adriano.margarin@gmail.com',
            'cpf': '01078740089',
            'cnh_type': ['A', 'B'],
            'password': '123456'
        }
        response = self.client.post(reverse_lazy('api-v1:customer-list'),
            data=data)
        content = json.loads(response.content)

        self.assertEqual(content['first_name'], data['first_name'])
        self.assertEqual(content['last_name'], data['last_name'])
        self.assertEqual(content['username'], data['username'])
        self.assertEqual(content['email'], data['email'])
        self.assertEqual(content['cpf'], data['cpf'])
        self.assertEqual(content['cnh_type'], data['cnh_type'])

    def test_create_cpf_invalid(self):
        data = {
            'first_name': 'Adriano',
            'last_name': 'Margarin',
            'username': 'adrianomargarin',
            'email': 'adriano.margarin@gmail.com',
            'cpf': '11111111111',
            'cnh_type': ['A', 'B'],
            'password': '123456'
        }
        response = self.client.post(reverse_lazy('api-v1:customer-list'),
            data=data)
        content = json.loads(response.content)

        self.assertEqual(content, {u'cpf': [u'CPF inv\xe1lido.']})

    def test_create_user_exists(self):
        data = {
            'first_name': 'Adriano',
            'last_name': 'Margarin',
            'username': 'cliente',
            'email': 'adriano.margarin@gmail.com',
            'cpf': '01078740089',
            'cnh_type': ['A', 'B'],
            'password': '123456'
        }
        response = self.client.post(reverse_lazy('api-v1:customer-list'),
            data=data)
        content = json.loads(response.content)

        self.assertEqual(content, {u'username':
            [u'Um usu\xe1rio com este nome de usu\xe1rio j\xe1 existe.']})

    def test_update(self):
        data = {
            'first_name': 'Adriano',
            'last_name': 'Margarin',
            'username': 'cliente',
            'email': 'adriano.margarin@gmail.com',
            'cpf': '01078740089',
            'cnh_type': ['A', 'B'],
            'password': '123456'
        }
        response = self.client.put(reverse_lazy('api-v1:customer-detail',
            args=[self.customer.id]), data=json.dumps(data),
            content_type='application/json', **self.headers)
        content = json.loads(response.content)

        self.assertEqual(content['first_name'], data['first_name'])
        self.assertEqual(content['last_name'], data['last_name'])
        self.assertEqual(content['username'], data['username'])
        self.assertEqual(content['email'], data['email'])
        self.assertEqual(content['cpf'], data['cpf'])
        self.assertEqual(content['cnh_type'], data['cnh_type'])

    def test_update_with_errors(self):
        data = {
            'first_name': 'Adriano',
            'last_name': 'Margarin',
            'username': 'cliente',
            'email': 'adriano.margarin@gmail.com',
            'cpf': '11111111111',
            'cnh_type': ['A', 'B'],
            'password': '123456'
        }
        response = self.client.put(reverse_lazy('api-v1:customer-detail',
            args=[self.customer.id]), data=json.dumps(data),
            content_type='application/json', **self.headers)
        content = json.loads(response.content)

        self.assertEqual(content, {u'cpf': [u'CPF inv\xe1lido.']})

    def test_partial_update(self):
        data = {
            'first_name': 'Adriano',
            'cnh_type': ['A', 'B', 'C'],
        }
        response = self.client.patch(reverse_lazy('api-v1:customer-detail',
            args=[self.customer.id]), data=json.dumps(data),
            content_type='application/json', **self.headers)
        content = json.loads(response.content)

        self.assertEqual(content['first_name'], data['first_name'])

    def test_destroy(self):
        response = self.client.delete(reverse_lazy('api-v1:customer-detail',
            args=[self.customer.id]), **self.headers)
        content = json.loads(response.content)

        self.assertEqual(content,
            {u'detail': u'Cliente exclu\xeddo com sucesso.'})
