# -*- coding: utf-8 -*-

from django.db import models
from app.customer.models import Customer
from app.fleet.models import Fleet


class RentACarManager(models.Manager):

    def rent(self, vehicle, customer):
        obj = self.create(vehicle=vehicle, customer=customer)
        vehicle.is_rented = True
        vehicle.save()

        return obj

    def give_back(self, rent_id, mileage_rotated):
        obj = self.get(id=rent_id)
        obj.mileage_rotated = mileage_rotated
        obj.is_back = True
        obj.save()

        obj.vehicle.is_rented = False
        obj.vehicle.save()

        return obj


class RentACar(models.Model):

    class Meta:
        app_label = u'rentacar'
        verbose_name = 'Aluguel'
        verbose_name_plural = 'Aluguéis'

    objects = RentACarManager()

    vehicle = models.ForeignKey(Fleet, verbose_name=u'Veículo')
    customer = models.ForeignKey(Customer, verbose_name=u'Cliente')
    mileage_rotated = models.DecimalField(verbose_name=u'Quilometragem rodada',
        max_digits=7, decimal_places=2, null=True, blank=True)
    is_back = models.BooleanField(verbose_name='Já foi devolvido?',
        default=False)

    def __unicode__(self):
        return self.vehicle.vehicle_name
