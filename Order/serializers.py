from rest_framework.serializers import ModelSerializer
from .models import *
from products.serializers import ProductSerializer


class FavoriteProductSerializer(ModelSerializer):
    class Meta:
        model = FavoriteProduct
        fields = '__all__'

    product = ProductSerializer()


class BasketSerializer(ModelSerializer):
    class Meta:
        model = Basket
        fields = '__all__'


class ProofoftransferSerializer(ModelSerializer):
    class Meta:
        model = Proofoftransfer
        fields = '__all__'


class SlipImageSerializer(ModelSerializer):
    class Meta:
        model = SilpImage
        fields = ['slip']


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
