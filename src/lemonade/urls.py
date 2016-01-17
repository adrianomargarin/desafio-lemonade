"""lemonade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView

from app.core.views import Home

# handler500 = 'app.core.views.page_500'
handler404 = 'app.core.views.page_404'
handler403 = 'app.core.views.page_403'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^clientes/', include('app.customer.urls', namespace='customer')),
    url(r'^administracao/', include('app.dashboard.urls',
        namespace='dashboard')),
    url(r'^frota/', include('app.fleet.urls', namespace='fleet')),
    url(r'^aluguel/', include('app.rentacar.urls', namespace='rentacar')),
    url(r'^login$', 'django.contrib.auth.views.login',
        {'template_name': 'login.html'}, name='login'),
    url(r'^logout$', 'django.contrib.auth.views.logout', {'next_page': '/'},
        name='logout'),
    url(r'^api/v1', include('app.api.v1.urls', namespace='api-v1')),
    url(r'^$', Home.as_view(), name='index'),
]
