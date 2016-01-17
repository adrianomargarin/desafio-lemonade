# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView
from app.fleet import views

urlpatterns = [
    # url(r'^$', views.FleetList.as_view(), name='list'),
    # url(r'^cadastrar$', views.FleetCreate.as_view(), name='create'),
    # url(r'^editar/(?P<pk>[0-9]+)$', views.FleetUpdate.as_view(),
    #     name='update'),
]
