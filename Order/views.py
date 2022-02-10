from django.shortcuts import render
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


# Create your views here.
class BasketView(ModelViewSet):
    queryset = Basket.objects.order_by('pk')
    serializer_class = BasketSerializer


class PaymentView(ModelViewSet):
    queryset = Payment.objects.order_by('pk')
    serializer_class = PaymentSerializer
