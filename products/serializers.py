from rest_framework.serializers import ModelSerializer
from .models import *
from drf_writable_nested import WritableNestedModelSerializer


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SubCategorySerializer(ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'

    category = CategorySerializer(read_only=True)


class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = Productimages
        fields = '__all__'

class ProductImageSerializer2(ModelSerializer):
    class Meta:
        model = Productimages
        fields = ['id','image']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    subcategory = SubCategorySerializer(read_only=True, many=True)
    productimages = ProductImageSerializer(read_only=True, many=True)
