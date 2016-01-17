# -*- coding: utf-8 -*-

from django.contrib import messages
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied

from app.fleet.models import Fleet


# class FleetBaseView(object):

#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         if not self.request.user.has_perms(['fleet.add_fleet',
#             'fleet.change_fleet', 'fleet.delete_fleet']):

#             raise PermissionDenied

#         return super(FleetBaseView, self).dispatch(*args, **kwargs)


# class FleetList(FleetBaseView, ListView):

#     model = Fleet
#     template_name = "fleet/list.html"

#     def get_queryset(self):
#         return Fleet.objects.all()


# class FleetCreate(FleetBaseView, CreateView):

#     model = Fleet
#     template_name = "fleet/form.html"
#     success_url = reverse_lazy('fleet:list')
#     fields = ['name', 'category', 'description']

#     def form_valid(self, form):
#         messages.success(self.request, u"Veículo cadastrado com sucesso.")

#         return super(FleetCreate, self).form_valid(form)


# class FleetUpdate(FleetBaseView, UpdateView):

#     model = Fleet
#     template_name = "fleet/form.html"
#     success_url = reverse_lazy('fleet:list')
#     fields = ['name', 'category', 'description']

#     def form_valid(self, form):
#         messages.success(self.request, u"Veículo alterado com sucesso.")

#         return super(FleetUpdate, self).form_valid(form)
