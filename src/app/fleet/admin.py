# -*- coding: utf-8 -*-

from django.contrib import admin
from app.fleet.models import Fleet


class FleetAdmin(admin.ModelAdmin):

    model = Fleet

admin.site.register(Fleet, FleetAdmin)
