# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from app.rentacar import views

urlpatterns = [
    url(r'^alugar$', login_required(views.RentACarView.as_view()),
        name='create'),
    url(r'^devolver$', login_required(views.RentACarGiveBackView.as_view()),
        name='give-back'),
]
