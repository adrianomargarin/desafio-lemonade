# -*- coding: utf-8 -*-

from rest_framework import serializers
from app.customer.models import Customer
from app.core.flags import CNH_CHOICES

class CustomerSerializer(serializers.ModelSerializer):

    cnh_type = serializers.MultipleChoiceField(choices=CNH_CHOICES)

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'username', 'email', 'cpf',
            'cnh_type', 'password')


class CustomerRetrieveSerializer(CustomerSerializer):

    class Meta:
        model = Customer
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'cpf',
            'cnh_type')
