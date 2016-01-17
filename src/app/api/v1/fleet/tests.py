# -*- coding: utf-8 -*-

import json
from base64 import b64encode
from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from app.core.test_helpers import Helper


class FleetTestCase(Helper, TestCase):

    def setUp(self):
        super(FleetTestCase, self).setUp()

        user_pass = b64encode(
            self.superuser.username + ':' + 'admin').decode('ascii')
        self.headers = {'HTTP_AUTHORIZATION': 'Basic %s' % user_pass}

    def test_retrieve(self):
        response = self.client.get(reverse_lazy('api-v1:fleet-detail',
            args=[self.vehicle.id]), **self.headers)
        content = json.loads(response.content)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['id'], self.vehicle.id)
        self.assertEqual(content['category'], self.vehicle.get_category_display())
        self.assertEqual(content['description'], self.vehicle.description)
        self.assertEqual(content['is_rented'], self.vehicle.is_rented)
        self.assertEqual(content['vehicle_name'], self.vehicle.vehicle_name)

    def test_create(self):
        data = {
            u'category': u'car',
            u'vehicle_name': u'Palio'
        }
        response = self.client.post(reverse_lazy('api-v1:fleet-list'),
            data=json.dumps(data), content_type='application/json', **self.headers)
        content = json.loads(response.content)

        self.assertEqual('Carro', content['category'])
        self.assertEqual(data['vehicle_name'], content['vehicle_name'])

    def test_create_with_error(self):
        data = {
            u'vehicle_name': u'Palio'
        }
        response = self.client.post(reverse_lazy('api-v1:fleet-list'),
            data=json.dumps(data), content_type='application/json', **self.headers)
        content = json.loads(response.content)

        self.assertEqual(content,
            {u'category': [u'Este campo \xe9 obrigat\xf3rio.']})

    def test_update(self):
        data = {
            u'category': u'motorcycle',
            u'vehicle_name': u'Moto'
        }
        response = self.client.put(reverse_lazy('api-v1:fleet-detail',
            args=[self.vehicle.id]), data=json.dumps(data),
            content_type='application/json', **self.headers)
        content = json.loads(response.content)

        self.assertEqual('Moto', content['category'])
        self.assertEqual(data['vehicle_name'], content['vehicle_name'])

    def test_update_with_error(self):
        data = {
            u'vehicle_name': u'Moto'
        }
        response = self.client.put(reverse_lazy('api-v1:fleet-detail',
            args=[self.vehicle.id]), data=json.dumps(data),
            content_type='application/json', **self.headers)
        content = json.loads(response.content)

        self.assertEqual(content,
            {u'category': [u'Este campo \xe9 obrigat\xf3rio.']})

    def test_partial_update(self):
        data = {
            u'category': u'motorcycle',
        }
        response = self.client.patch(reverse_lazy('api-v1:fleet-detail',
            args=[self.vehicle.id]), data=json.dumps(data),
            content_type='application/json', **self.headers)
        content = json.loads(response.content)

        self.assertEqual('Moto', content['category'])

    def test_destroy(self):
        response = self.client.delete(reverse_lazy('api-v1:fleet-detail',
            args=[self.vehicle.id]), content_type='application/json',
            **self.headers)
        content = json.loads(response.content)

        self.assertEqual(content, {'detail': u'Veículo excluído com sucesso.'})
