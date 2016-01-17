# -*- coding: utf-8 -*-

from decimal import Decimal
from model_mommy import mommy
from django.test import TestCase
from django.test.client import Client
from django.core.urlresolvers import reverse_lazy
from app.customer.models import Customer
from app.fleet.models import Fleet
from app.rentacar import models
from app.core.test_helpers import Helper


class ModelsTestCase(TestCase):

    def setUp(self):
        self.customer = mommy.make(Customer, cnh_type=['A'])
        self.vehicle = mommy.make(Fleet)

    def test_rent(self):
        rent = models.RentACar.objects.rent(vehicle=self.vehicle,
            customer=self.customer)

        self.assertTrue(self.vehicle.is_rented)

    def test_give_back(self):
        obj = models.RentACar.objects.rent(vehicle=self.vehicle,
            customer=self.customer)

        models.RentACar.objects.give_back(obj.id,
            mileage_rotated=Decimal("200.00"))

    def test_unicode(self):
        self.vehicle.vehicle_name = 'Palio'
        self.vehicle.save()
        rent = mommy.make(models.RentACar, vehicle=self.vehicle)

        self.assertEqual(rent.__unicode__(), 'Palio')


class ViewsTestCase(Helper, TestCase):

    def setUp(self):
        super(ViewsTestCase, self).setUp()

    def test_get_create(self):
        self.login()
        response = self.client.get(reverse_lazy('rentacar:create'))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, 'http://testserver/')

    def test_post_create(self):
        self.login()
        data = {'fleet_id': self.vehicle.id}
        response = self.client.post(reverse_lazy('rentacar:create'),
            data=data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,
            'http://testserver/administracao/meus-alugueis')
        self.assertEqual(models.RentACar.objects.filter(is_back=False).count(), 2)

    def test_post_create_is_rented(self):
        self.login()
        self.vehicle.is_rented = True
        self.vehicle.save()
        data = {'fleet_id': self.vehicle.id}
        response = self.client.post(reverse_lazy('rentacar:create'),
            data=data)

        self.assertTrue(response.cookies.get('messages'))
        self.assertEqual(models.RentACar.objects.filter(is_back=False).count(), 1)

    def test_get_update(self):
        self.login()
        response = self.client.get(reverse_lazy('rentacar:give-back'))

        self.assertEqual(response.url, 'http://testserver/administracao/meus-alugueis')

    def test_post_update(self):
        self.login()
        data = {
            'rent_id': self.rent.id,
            'mileage_rotated': 500.00
        }
        response = self.client.post(reverse_lazy('rentacar:give-back'),
            data=data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url,
            'http://testserver/administracao/meus-alugueis')
        self.assertEqual(models.RentACar.objects.filter(is_back=False).count(), 0)

    def test_post_update_with_error(self):
        self.login()
        data = {'rent_id': self.vehicle.id}
        response = self.client.post(reverse_lazy('rentacar:give-back'),
            data=data)

        self.assertTrue(response.cookies.get('messages'))
        self.assertEqual(models.RentACar.objects.filter(is_back=False).count(), 1)
