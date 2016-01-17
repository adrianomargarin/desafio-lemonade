# -*- coding: utf-8 -*-


from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from app.api.v1.customer.serializers import CustomerSerializer
from app.api.v1.customer.serializers import CustomerRetrieveSerializer
from app.customer.models import Customer


class CustomerView(viewsets.ViewSet):

    serializer_class = CustomerSerializer
    serializer_class_retrieve = CustomerRetrieveSerializer

    def get_single_object(self, request, pk):
        return get_object_or_404(Customer.objects.all(), pk=pk,
            username=request.user.username)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            obj = Customer.objects.create_user(
                first_name=serializer.data.get('first_name'),
                last_name=serializer.data.get('last_name'),
                username=serializer.data.get('username'),
                email=serializer.data.get('email'),
                cpf=serializer.data.get('cpf'),
                cnh_type=request.data.getlist('cnh_type'),
                password=serializer.data.get('password'),
            )

            return Response(self.serializer_class_retrieve(obj).data)

        return Response(serializer.errors)

    def update(self, request, pk=None, partial=None):
        obj = self.get_single_object(request, pk)
        serializer = self.serializer_class(data=request.data, instance=obj,
            partial=partial)

        if serializer.is_valid():
            obj.first_name = request.data.get('first_name') or serializer.data.get('first_name')
            obj.last_name = request.data.get('last_name') or serializer.data.get('last_name')
            obj.username = request.data.get('username') or serializer.data.get('username')
            obj.email = request.data.get('email') or serializer.data.get('email')
            obj.cpf = request.data.get('cpf') or serializer.data.get('cpf')
            obj.cnh_type = list(request.data.get('cnh_type')) or list(serializer.data.get('cnh_type'))

            if request.data.get('password'):
                obj.set_password(request.data.get('password'))

            obj.save()

            if serializer.data.get('password'):
                serializer.instance.set_password(serializer.data.get('password'))

            return Response(self.serializer_class_retrieve(obj).data)

        return Response(serializer.errors)

    def partial_update(self, request, pk=None):
        return self.update(request, pk=pk, partial=True)

    def destroy(self, request, pk=None):
        obj = self.get_single_object(request, pk)
        obj.delete()

        return Response({'detail': 'Cliente excluído com sucesso.'})

    def retrieve(self, request, pk=None):
        obj = self.get_single_object(request, pk)
        serializer = self.serializer_class_retrieve(obj)

        return Response(serializer.data)

