from api.models import Shop
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from api.serializers import ShopSerializer
from rest_framework.response import Response
from api.resources.serializers import ShopSerializer, ErrorSerializer


class ShopViewSet(viewsets.ViewSet):

    def list(self, request):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops, many=True)

        return Response(serializer.data)

    def create(self, request):
        shop = request.data.get('shop')
        serializer = ShopSerializer(data=shop)

        if serializer.is_valid(raise_exception=True):
            Shop.objects.create(title=shop['title'])

            return Response(serializer.data)

        else:
            data = {'error': 'Error Creating Shop', 'status_code': 400}
            error_serializer = ErrorSerializer(data=data)
            error_serializer.is_valid(True)

            return Response(error_serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Shop.objects.all()
        shop = get_object_or_404(queryset, pk=pk)
        serializer = ShopSerializer(shop)

        return Response(serializer.data)

    def update(self, request, pk=None):
        shop_to_update = request.data.get('shop')
        serializer = ShopSerializer(data=shop_to_update)

        if serializer.is_valid(raise_exception=True):
            queryset = Shop.objects.all()
            shop = get_object_or_404(queryset, pk=pk)
            shop.title = shop_to_update['title']
            shop.save()

            serializer_to_return = ShopSerializer(shop)

            return Response(serializer_to_return.data)

        else:
            data = {'error': 'Error Updating Shop', 'status_code': 400}
            error_serializer = ErrorSerializer(data=data)
            error_serializer.is_valid(True)

            return Response(error_serializer.data)

    def destroy(self, request, pk=None):
        queryset = Shop.objects.all()
        shop = get_object_or_404(queryset, pk=pk)
        title = shop.title

        shop.delete()

        return Response({"Success": "Shop '{}' deleted successfully".format(title)})
