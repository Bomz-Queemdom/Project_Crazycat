from rest_framework.serializers import ModelSerializer
from .models import *
from products.serializers import ProductSerializer
from account.serializers import *


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


class SlipImageEditSerializer(ModelSerializer):
    class Meta:
        model = SilpImage
        fields = '__all__'


class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

    customer = CustomerSerializer(read_only=True)
    address = AddressSerializer(read_only=True)


class PaymentSerEditializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
