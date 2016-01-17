# -*- coding: utf-8 -*-

from base64 import b64encode
from rest_framework.test import APIRequestFactory
from django.contrib.auth.models import User
from app.customer.models import Customer
from app.fleet.models import Fleet
from app.rentacar.models import RentACar


class Helper(object):

    def setUp(self):
        self.superuser = User.objects.create_superuser(username='admin_test',
            email='teste@teste.com', password='admin')

        self.customer = Customer.objects.create(username='cliente',
            cnh_type=['B'])
        self.customer.set_password('cliente')
        self.customer.save()

        user_pass = b64encode(
            self.customer.username + ':' + 'cliente').decode('ascii')

        self.headers = {'HTTP_AUTHORIZATION': 'Basic %s' % user_pass}

        self.factory = APIRequestFactory()
        # self.request = self.factory.get(reverse('api-v1:emitter-list'),
        #     **self.headers)

        self.vehicle = Fleet.objects.create(vehicle_name='Palio',
            category='car')

        self.rent = RentACar.objects.create(vehicle=self.vehicle,
            customer=self.customer)

    def login(self):
        self.client.login(username=self.customer.username, password='cliente')
