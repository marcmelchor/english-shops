from rest_framework import serializers
from api.models import Product, Shop


class ShopSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Shop
        fields = ('id', 'title')


class ProductSerializer(serializers.HyperlinkedModelSerializer):

    shop_name = ShopSerializer(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'shop_name', 'title', 'link', 'description')


class ErrorSerializer(serializers.Serializer):
    error = serializers.CharField()
    status_code = serializers.IntegerField()
