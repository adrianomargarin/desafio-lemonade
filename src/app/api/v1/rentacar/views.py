# -*- coding: utf-8 -*-


from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from app.api import mixins
from app.api.v1.rentacar.serializers import RentACarSerializer
from app.api.v1.rentacar.serializers import RentACarRetrieveSerializer
from app.api.v1.rentacar.serializers import RentACarGiveBackSerializer
from app.fleet.models import Fleet
from app.rentacar.models import RentACar


class RentACarBaseView(viewsets.ViewSet):

    serializer_class_retrieve = RentACarRetrieveSerializer

    def get_single_object(self, pk, request, is_back=False):
        return get_object_or_404(RentACar.objects.all(), pk=pk)


class RentACarView(RentACarBaseView):

    serializer_class = RentACarSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data,
            context={'customer': request.user.customer})

        if serializer.is_valid():
            vehicle = Fleet.objects.get(pk=serializer.data.get('vehicle'))
            obj = RentACar.objects.rent(vehicle, request.user.customer)

            return RentACarRetrieveSerializer().retrieve(request, pk=obj.pk)

        return Response(serializer.errors)


class RentACarGiveBack(RentACarBaseView):

    serializer_class = RentACarGiveBackSerializer

    def update(self, request, pk=None, partial=None):
        obj = self.get_single_object(pk, request)
        serializer = self.serializer_class(data=request.data, instance=obj,
            partial=partial)

        if serializer.is_valid():
            obj = RentACar.objects.give_back(obj.id, request.data.get('mileage_rotated'))

            return RentACarRetrieveSerializer().retrieve(request, pk=obj.pk)

        return Response(serializer.errors)


class RentACarRetrieveSerializer(RentACarBaseView):

    def retrieve(self, request, pk=None):
        obj = self.get_single_object(pk, request)
        serializer = self.serializer_class_retrieve(obj)

        return Response(serializer.data)
