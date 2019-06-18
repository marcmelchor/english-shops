from api.models import Product, Shop
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from api.serializers import ProductSerializer, ErrorSerializer
from rest_framework.response import Response


class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)

        return Response(serializer.data)

    def create(self, request):
        product = request.data.get('product')
        serializer = ProductSerializer(data=product)

        if serializer.is_valid(raise_exception=True):
            db_product = Product.objects.create(product)
            product_serializer = ProductSerializer(db_product)

            return Response(product_serializer.data)

        else:
            data = {'error': 'Error Creating Product', 'status_code': 400}
            error_serializer = ErrorSerializer(data=data)
            error_serializer.is_valid(True)

            return Response(error_serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(product)

        return Response(serializer.data)

    def update(self, request, pk=None):
        product_to_update = request.data.get('product')
        serializer = ProductSerializer(data=product_to_update)

        if serializer.is_valid(raise_exception=True):
            queryset = Product.objects.all()
            product = get_object_or_404(queryset, pk=pk)

            if product_to_update['shop_name'] and product_to_update['shop_name'].isnumeric() and \
                    Shop.objects.get(pk=product_to_update['shop_name']):
                product.shop_name = product_to_update['shop_name']

            if product_to_update['title']:
                product.title = product_to_update['title']

            if product_to_update['link']:
                product.link = product_to_update['link']

            if product_to_update['description']:
                product.description = product_to_update['description']

            if product_to_update['image_link']:
                product.image_link = product_to_update['image_link']

            product.save()
            serializer_to_return = ProductSerializer(product)

            return Response(serializer_to_return.data)

        else:
            data = {'error': 'Error Updating Product', 'status_code': 400}
            error_serializer = ErrorSerializer(data=data)
            error_serializer.is_valid(True)

            return Response(error_serializer.data)

    def destroy(self, request, pk=None):
        queryset = Product.objects.all()
        product = get_object_or_404(queryset, pk=pk)
        title = product.title

        product.delete()

        return Response({"Success": "Product '{}' deleted successfully".format(title)})
