# -*- coding: utf-8 -*-


from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from app.api import mixins
from app.api.v1.fleet.serializers import FleetSerializer
from app.api.v1.fleet.serializers import FleetRetrieveSerializer
from app.fleet.models import Fleet


# class FleetView(viewsets.ViewSet, mixins.ListMixin):
class FleetView(viewsets.ViewSet):

    serializer_class = FleetSerializer
    serializer_class_retrieve = FleetRetrieveSerializer

    # def get_queryset(self):
    #     return Fleet.objects.all()

    def get_single_object(self, pk):
        return get_object_or_404(Fleet.objects.all(), pk=pk)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return self.retrieve(request, pk=serializer.instance.id)

        return Response(serializer.errors)

    def update(self, request, pk=None, partial=None):
        obj = self.get_single_object(pk)
        serializer = self.serializer_class(data=request.data, instance=obj,
            partial=partial)

        if serializer.is_valid():
            serializer.save()

            return self.retrieve(request, pk=serializer.instance.id)

        return Response(serializer.errors)

    def partial_update(self, request, pk=None):
        return self.update(request, pk=pk, partial=True)

    def destroy(self, request, pk=None):
        obj = self.get_single_object(pk)
        obj.delete()

        return Response({'detail': 'Veículo excluído com sucesso.'})

    # def list(self, request):
    #     from rest_framework.pagination import Response as ResponseList
    #     serializer = self.serializer_class(Fleet.objects.all())

    #     return ResponseList(serializer.data)

    def retrieve(self, request, pk=None):
        obj = self.get_single_object(pk)
        serializer = self.serializer_class_retrieve(obj)

        return Response(serializer.data)

