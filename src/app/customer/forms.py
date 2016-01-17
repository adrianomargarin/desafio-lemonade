# -*- coding: utf-8 -*-

from django import forms
from app.customer.models import Customer


class CustomerForm(forms.ModelForm):

    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'username', 'email', 'cpf',
            'cnh_type', 'password', 'password2']
        widgets = {
            'password': forms.PasswordInput()
        }

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    def clean(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")

        if password != password2:
            raise forms.ValidationError(u"As senhas não conferem.")

        return super(CustomerForm, self).clean()
