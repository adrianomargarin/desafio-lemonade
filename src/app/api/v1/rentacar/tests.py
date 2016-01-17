# -*- coding: utf-8 -*-

import json
from base64 import b64encode
from django.test import TestCase
from django.core.urlresolvers import reverse_lazy
from app.core.test_helpers import Helper


class RentACarTestCase(Helper, TestCase):

    def setUp(self):
        super(RentACarTestCase, self).setUp()

    def test_create(self):
        data = {
            'vehicle': self.vehicle.id
        }
        response = self.client.post(reverse_lazy('api-v1:rentacar-create-list'),
            data=json.dumps(data), content_type='application/json',
            **self.headers)
        content = json.loads(response.content)

        self.assertEqual(content['customer'], self.customer.id)
        self.assertEqual(content['vehicle'], self.vehicle.id)

    def test_create_with_error(self):
        self.vehicle.is_rented = True
        self.vehicle.save()
        data = {
            'vehicle': self.vehicle.id
        }
        response = self.client.post(reverse_lazy('api-v1:rentacar-create-list'),
            data=json.dumps(data), content_type='application/json',
            **self.headers)
        content = json.loads(response.content)

        self.assertEqual(content,
            {u'vehicle': [u'Ve\xedculo Palio j\xe1 alugado.']})

    def test_update(self):
        data = {
            'vehicle': self.vehicle.id,
            'mileage_rotated': 500.00
        }
        response = self.client.put(reverse_lazy('api-v1:rentacar-update-detail',
            args=[self.rent.id]), data=json.dumps(data),
            content_type='application/json', **self.headers)
        content = json.loads(response.content)

        self.assertEqual(content['customer'], self.customer.id)
        self.assertEqual(content['vehicle'], self.vehicle.id)
        self.assertEqual(content['mileage_rotated'], '500.00')

    def test_update_with_error(self):
        data = {
            'vehicle': 999
        }
        response = self.client.put(reverse_lazy('api-v1:rentacar-update-detail',
            args=[self.rent.id]), data=json.dumps(data),
            content_type='application/json', **self.headers)
        content = json.loads(response.content)

        self.assertEqual(content,
            {u'vehicle': [u'Pk inv\xe1lido "999" - objeto n\xe3o existe.']})
