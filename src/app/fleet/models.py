# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from app.core.flags import CATEGORY_CHOICES


class Fleet(models.Model):

    class Meta:
        app_label = u'fleet'
        verbose_name = 'Frota'
        verbose_name_plural = 'Frotas'

    vehicle_name = models.CharField(verbose_name=u'Nome', max_length=255)
    category = models.CharField(verbose_name=u'Categoria', max_length=10,
        choices=CATEGORY_CHOICES)
    description = models.TextField(verbose_name=u'Descrição', max_length=1000,
        null=True, blank=True)
    is_rented = models.BooleanField(verbose_name=u'Está alugado?',
        default=False)

    def _validate_cnh_type(self, customer):
        can_rent = False

        if self.category == 'motorcycle' and 'A' in customer.cnh_type:
            can_rent = True
        elif self.category == 'car' and 'B' in customer.cnh_type:
            can_rent = True
        elif self.category == 'utility' and 'C' in customer.cnh_type:
            can_rent = True
        elif (self.category == 'truck' and
            ('D' in customer.cnh_type or 'E' in customer.cnh_type)):
            can_rent = True

        return can_rent

    def can_rent(self, customer):
        if not self.is_rented:
            return self._validate_cnh_type(customer)

    def __unicode__(self):
        return self.vehicle_name
