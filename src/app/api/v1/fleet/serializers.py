# -*- coding: utf-8 -*-

from rest_framework import serializers
from app.fleet.models import Fleet
from app.core.flags import CNH_CHOICES


class FleetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fleet
        exclude = ['is_rented']


class FleetRetrieveSerializer(FleetSerializer):

    category = serializers.SerializerMethodField('get_category_display')

    def get_category_display(self, obj):
        return obj.get_category_display()

    class Meta:
        model = Fleet
        fields = ['id', 'vehicle_name', 'category', 'description', 'is_rented']
