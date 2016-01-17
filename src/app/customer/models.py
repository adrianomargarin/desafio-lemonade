# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from multiselectfield import MultiSelectField
from app.core.flags import CNH_CHOICES
from app.core.utils import CPF
from app.core.validators import validate_cpf


class Customer(User):

    class Meta:
        app_label = u'customer'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    cpf = models.CharField(verbose_name=u'CPF', max_length=11, unique=True,
        validators=[validate_cpf])
    cnh_type = MultiSelectField(verbose_name=u'Tipo da CNH', max_length=9,
        choices=CNH_CHOICES, max_choices=5)

    def format_cpf(self):
        return CPF(self.cpf).format()

    def __unicode__(self):
        return self.get_full_name() or self.username
