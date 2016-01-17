# -*- coding: utf-8 -*-

from django.conf.urls import url, include, patterns
from rest_framework import routers
from app.api.v1.fleet.views import FleetView
from app.api.v1.customer.views import CustomerView
from app.api.v1.rentacar.views import RentACarView
from app.api.v1.rentacar.views import RentACarGiveBack
from app.api.v1.rentacar.views import RentACarRetrieveSerializer


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'/frota', FleetView, base_name="fleet")
router.register(r'/cliente', CustomerView, base_name="customer")
router.register(r'/alugueis', RentACarRetrieveSerializer, base_name='rentacar')
router.register(r'/alugar', RentACarView, base_name="rentacar-create")
router.register(r'/devolver', RentACarGiveBack, base_name="rentacar-update")

fleet_detail = FleetView.as_view({
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

customer_detail = CustomerView.as_view({
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

rentacar_detail = RentACarGiveBack.as_view({
    'put': 'update',
})

urlpatterns = patterns('',
    url(r'^/frota/(?P<pk>[0-9]+)/$', fleet_detail, name='fleet-detail'),
    url(r'^/cliente/(?P<pk>[0-9]+)/$', customer_detail, name='customer-detail'),
    url(r'^/aluguel/(?P<pk>[0-9]+)/$', rentacar_detail, name='rentacar-detail'),
)

urlpatterns += router.urls
