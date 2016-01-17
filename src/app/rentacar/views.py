# -*- coding: utf-8 -*-

from django.contrib import messages
from django.views.generic import View
from django.views.generic.edit import CreateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from app.rentacar.models import RentACar
from app.fleet.models import Fleet


class RentACarView(CreateView):

    model = RentACar

    def get(self, request):
        return HttpResponseRedirect(reverse_lazy('index'))

    def post(self, request):
        vehicle = Fleet.objects.get(id=request.POST.get('fleet_id'))

        if vehicle.can_rent(request.user.customer):
            RentACar.objects.rent(vehicle, request.user.customer)

            messages.success(request, u'Veículo %s alugado com sucesso.' %
                vehicle.vehicle_name)

            return HttpResponseRedirect(reverse_lazy('dashboard:rent'))
        else:
            messages.warning(request, u'Veículo %s já alugado.' % vehicle.vehicle_name)

            return HttpResponseRedirect(reverse_lazy('index'))



class RentACarGiveBackView(CreateView):

    model = RentACar

    def get(self, request):
        return HttpResponseRedirect(reverse_lazy('dashboard:rent'))

    def post(self, request):
        mileage_rotated = request.POST.get('mileage_rotated')
        rent = RentACar.objects.get(id=request.POST.get('rent_id'))

        if not mileage_rotated:
            messages.warning(request,
                u'Informe a quilometragem rodada do veículo %s.' %
                    rent.vehicle.vehicle_name)
        else:
            RentACar.objects.give_back(rent_id=request.POST.get('rent_id'),
                mileage_rotated=mileage_rotated)

            messages.success(request, u'Veículo %s devolvido com sucesso.' %
                rent.vehicle.vehicle_name)

        return HttpResponseRedirect(reverse_lazy('dashboard:rent'))
