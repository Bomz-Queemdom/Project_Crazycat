from django.shortcuts import render

# Create your views here.
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from account.serializers import *

class AddressView(ModelViewSet):
    queryset = Address.objects.order_by('pk')
    serializer_class = AddressSerializer