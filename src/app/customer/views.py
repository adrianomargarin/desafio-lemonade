# -*- coding: utf-8 -*-

from django.contrib import messages
from django.views.generic.edit import CreateView
from django.core.urlresolvers import reverse_lazy
from app.customer import forms
from app.customer import models


class CustomerCreate(CreateView):

    template_name = "customer/customer_form.html"
    form_class = forms.CustomerForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.instance.set_password(form.cleaned_data.get("password"))
        messages.success(self.request, u"Cadastro efetuado com sucesso.")

        return super(CustomerCreate, self).form_valid(form)
