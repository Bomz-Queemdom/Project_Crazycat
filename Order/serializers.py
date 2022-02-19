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

    product = ProductSerializer()


class SlipImageSerializer(ModelSerializer):
    class Meta:
        model = SilpImage
        fields = ['slip', 'proofoftransfer']


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    paymentimage = SlipImageSerializer()
