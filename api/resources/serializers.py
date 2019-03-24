from rest_framework import serializers
from api.models import Shop, Product
import json


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        title = serializers.CharField(source='_title')
        fields = ('id', 'title')

        def create(self, validate_date):
            print(Shop.objects.create(**validate_date))
            return Shop.objects.create(**validate_date)


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        title = serializers.CharField(source='_title')
        link = serializers.CharField(source='_link')
        description = serializers.CharField(source='_description')
        image_link = serializers.CharField(source='_image_link')
        fields = ('shop_name', 'id', 'title', 'link', 'description', 'image_link')

    shop_name = serializers.SerializerMethodField('get_shop_title')

    def get_shop_title(self, obj):
        return obj._shop_name._title


class ErrorSerializer(serializers.Serializer):
    error = serializers.CharField()
    status_code = serializers.IntegerField()
