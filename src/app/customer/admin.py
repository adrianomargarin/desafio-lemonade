# -*- coding: utf-8 -*-

from django.contrib import admin
from app.customer.models import Customer


class CustomerAdmin(admin.ModelAdmin):

    model = Customer

admin.site.register(Customer, CustomerAdmin)
