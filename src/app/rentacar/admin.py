# -*- coding: utf-8 -*-

from django.contrib import admin
from app.rentacar.models import RentACar


class RentACarAdmin(admin.ModelAdmin):

    model = RentACar
    list_display = ['id', 'vehicle', 'customer', 'is_back']


admin.site.register(RentACar, RentACarAdmin)
