# -*- coding: utf-8 -*-

from model_mommy import mommy
from django.test import TestCase
from app.customer.models import Customer
from app.fleet import models


class ModelsTestCase(TestCase):

    def setUp(self):
        self.customer = mommy.make(Customer, cnh_type=['A'])
        self.vehicle = mommy.make(models.Fleet)

    def test_validate_cnh_type_a_motorcycle_true(self):
        self.vehicle.category = 'motorcycle'
        self.vehicle.save()

        self.assertTrue(self.vehicle._validate_cnh_type(self.customer))

    def test_validate_cnh_type_b_car_true(self):
        self.customer.cnh_type = ['B']
        self.customer.save()
        self.vehicle.category = 'car'
        self.vehicle.save()

        self.assertTrue(self.vehicle._validate_cnh_type(self.customer))

    def test_validate_cnh_type_c_utility_true(self):
        self.customer.cnh_type = ['C']
        self.customer.save()
        self.vehicle.category = 'utility'
        self.vehicle.save()

        self.assertTrue(self.vehicle._validate_cnh_type(self.customer))

    def test_validate_cnh_type_d_truck_true(self):
        self.customer.cnh_type = ['D']
        self.customer.save()
        self.vehicle.category = 'truck'
        self.vehicle.save()

        self.assertTrue(self.vehicle._validate_cnh_type(self.customer))

    def test_validate_cnh_type_e_truck_true(self):
        self.customer.cnh_type = ['E']
        self.customer.save()
        self.vehicle.category = 'truck'
        self.vehicle.save()

        self.assertTrue(self.vehicle._validate_cnh_type(self.customer))

    def test_validate_cnh_type_false(self):
        self.vehicle.category = 'car'
        self.vehicle.save()

        self.assertFalse(self.vehicle._validate_cnh_type(self.customer))


    def test_can_rent(self):
        self.vehicle.category = 'motorcycle'
        self.vehicle.save()

        self.assertTrue(self.vehicle.can_rent(self.customer))

    def test_unicode(self):
        self.vehicle.vehicle_name = 'Palio'
        self.vehicle.save()

        self.assertEqual(self.vehicle.__unicode__(), 'Palio')
