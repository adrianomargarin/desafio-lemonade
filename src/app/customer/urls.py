# -*- coding: utf-8 -*-

from django.conf.urls import url
from django.views.generic import TemplateView
from app.customer import views


urlpatterns = [
    url(r'^registro/$', views.CustomerCreate.as_view(), name='register'),
]
