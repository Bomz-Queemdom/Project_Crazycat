from rest_framework.serializers import ModelSerializer
from .models import *


class CustomerSerializer(ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = '__all__'


class AddressSerializer(ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
