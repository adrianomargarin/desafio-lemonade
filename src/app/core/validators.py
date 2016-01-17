# -*- coding: utf-8 -*-

from django.core.exceptions import ValidationError
from app.core.utils import CPF

def validate_cpf(value):
    if not CPF(value).validate():
        raise ValidationError("CPF inválido.")
