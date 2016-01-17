# -*- coding: utf-8 -*-

from rest_framework import serializers
from app.rentacar.models import RentACar


class RentACarSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentACar
        fields = ('vehicle',)

    def validate_vehicle(self, obj):
        if not obj.can_rent(self.context.get('customer')):
            raise serializers.ValidationError(u'Veículo %s já alugado.' % obj.vehicle_name)

        return obj


class RentACarGiveBackSerializer(serializers.ModelSerializer):

    class Meta:
        model = RentACar
        fields = ('vehicle', 'mileage_rotated')


class RentACarRetrieveSerializer(RentACarSerializer):

    class Meta:
        model = RentACar
        fields = ('id', 'vehicle', 'customer', 'mileage_rotated')
