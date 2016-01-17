# -*- coding: utf-8 -*-

from django.core.paginator import EmptyPage
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from rest_framework.settings import api_settings


# class PaginateMixin(object):
#     """
#     Mixin for paginate the API list resourses
#     This mixin receive a queryset and a request
#     and return a paginated queryset
#     """
#     paginate_by = 20
#     paginate_class = api_settings.DEFAULT_PAGINATION_CLASS

#     def paginate_api(self, queryset, request):
#         paginator = Paginator(queryset, self.paginate_by)
#         page = request.query_params.get('page')

#         try:
#             queryset = paginator.page(page)
#         except PageNotAnInteger:
#             queryset = paginator.page(1)
#         except EmptyPage:
#             queryset = paginator.page(paginator.num_pages)

#         return queryset


# class ListMixin(PaginateMixin):
#     """
#     Mixin for list resourses
#     This mixin get a list of objects based on the
#     queryset and return a paginated list of objects
#     """
#     def list(self, request, queryset = None):
#         serializer_class = self.serializer_class

#         if queryset == None:
#             queryset = self.get_queryset(request)

#         if hasattr(self, 'serializer_retrieve_class'):
#             serializer_class = self.serializer_retrieve_class

#         objs = self.paginate_api(queryset, request)
#         from IPython import embed; embed()
#         serializer = self.paginate_class(objs, serializer_class, context = {'request': self.request})

#         return Response(serializer.data)
