# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from app.fleet.models import Fleet

def page_403(request):
    response = render(request, '403.html')
    response.status_code = 403

    return response

class Home(ListView):

    template_name='fleet_list.html'

    def get_queryset(self, *args, **kwargs):
        return Fleet.objects.all()
