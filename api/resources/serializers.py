from rest_framework import serializers
from api.models import Shop, Product
import json


class ShopSerializer(serializers.ModelSerializer):

    class Meta:
        model = Shop
        title = serializers.CharField(source='_title')
        fields = ('id', 'title')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        title = serializers.CharField(source='_title')
        link = serializers.CharField(source='_link')
        description = serializers.CharField(source='_description')
        image_link = serializers.CharField(source='_image_link')
        fields = ('id', 'shop_name', 'title', 'link', 'description', 'image_link')

    shop_name = serializers.SerializerMethodField('get_shop_title')

    def get_shop_title(self, obj):
        return obj._shop_name._title


class ShopJSON:

    @staticmethod
    def get_json_shop(db_shop):
        json_data = []
        for shop in db_shop:

            json_data.append({'id': shop.id, })
            # print(json_data)

        json_output = json.dumps(json_data)
        return json_output
