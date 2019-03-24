from api.models import Product, Shop
from rest_framework.views import APIView
from rest_framework.response import Response
from api.resources.serializers import ProductSerializer


class ProductView(APIView):

    def get(self, request, *args, **kwargs):
        if 'product_id' in kwargs:
            product_id = kwargs['product_id']

            if Shop.objects.filter(pk=product_id):
                db_product = Shop.objects.get(pk=product_id)
                serializer = ProductSerializer(db_product)
                return Response(serializer.data)
            else:
                return Response('Product does not exist')
        else:
            is_limited = False
            start = request.GET.get('start', None)
            end = request.GET.get('end', None)
            if start and end:
                if not start.isnumeric() or not end.isnumeric():
                    return Response('Must Pass Valid Numbers')

                start_nun = int(start)
                end_num = int(end)
                is_limited = True

            if is_limited:
                db_product = Product.objects.all()[start_nun: end_num]
                serializer = ProductSerializer(db_product, many=True)
                return Response(serializer.data)
            else:
                db_product = Product.objects.all()
                serializer = ProductSerializer(db_product, many=True)
                return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        pass


class ProductsInShopView(APIView):

    def get(self, request, *args, **kwargs):
        if 'shop_id' in kwargs:
            shop_id = kwargs['shop_id']

            if Shop.objects.filter(pk=shop_id):
                is_limited = False
                start = request.GET.get('start', None)
                end = request.GET.get('end', None)
                if start and end:
                    if not start.isnumeric() or not end.isnumeric():
                        return Response('Must Pass Valid Numbers')

                    start_num = int(start)
                    end_num = int(end)
                    is_limited = True

                if is_limited:
                    db_product = Product.objects.filter(_shop_name_id=shop_id)[start_num: end_num]
                    serializer = ProductSerializer(db_product, many=True)
                    return Response(serializer.data)
                else:
                    db_product = Product.objects.filter(_shop_name_id=shop_id)
                    serializer = ProductSerializer(db_product, many=True)
                    return Response(serializer.data)

            else:
                return Response('Product does not exist')

        else:
            return Response('Must Pass Shop Id')
