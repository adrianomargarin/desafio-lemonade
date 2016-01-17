# -*- coding: utf-8 -*-

from django.views.generic.list import ListView
from app.rentacar.models import RentACar


class RentACarList(ListView):

    model = RentACar
    template_name = "dashboard/list-rent.html"

    def get_queryset(self):
        return RentACar.objects.filter(customer=self.request.user.customer)
