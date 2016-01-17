# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from app.dashboard import views

urlpatterns = [
    url(r'^$', login_required(TemplateView.as_view(
        template_name='dashboard/index.html')), name='index'),
    url(r'^meus-alugueis$', login_required(views.RentACarList.as_view()), name='rent')
]
