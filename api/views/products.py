from api.models import Product, Shop
from rest_framework.views import APIView
from rest_framework.response import Response
from api.resources.serializers import ProductSerializer, ErrorSerializer
import http.client


class ProductView(APIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        if 'product_id' in kwargs:
            product_id = kwargs['product_id']

            if Shop.objects.filter(pk=product_id):
                db_product = Shop.objects.get(pk=product_id)
                serializer = ProductSerializer(db_product)
                return Response(serializer.data)
            else:
                data = {'error': 'Product does not exist', 'status_code': 404}
                error_serializer = ErrorSerializer(data=data)
                error_serializer.is_valid(True)
                return Response(error_serializer.data)
        else:
            is_limited = False
            start = request.GET.get('start', None)
            end = request.GET.get('end', None)
            if start and end:
                if not start.isnumeric() or not end.isnumeric():
                    data = {'error': 'Must Pass Valid Numbers', 'status_code': 400}
                    error_serializer = ErrorSerializer(data=data)
                    error_serializer.is_valid(True)
                    return Response(error_serializer.data)

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
        product = request.data.get('product')
        if product["shop_name"]:
            if Product.objects.filter(shop_name=product["shop_name"]):
                serializer = ProductSerializer(data=product)
                if serializer.is_valid(raise_exception=True):
                    product_saved = Product()
                    product_saved.shop_name = product["shop_name"]
                    product_saved.title = product["title"]
                    product_saved.link = product["link"]
                    product_saved.description = product["description"]
                    product_saved.image_link = product["image_link"]
                    product_saved.save()

                    return Response({"Success": "Product '{}' created successfully".format(product_saved.title)})

                else:
                    data = {'error': 'Error Creating Shop', 'status_code': 400}
                    error_serializer = ErrorSerializer(data=data)
                    error_serializer.is_valid(True)
                    return Response(error_serializer.data)

            else:
                data = {'error': 'Shop Does Not Exist', 'status_code': 400}
                error_serializer = ErrorSerializer(data=data)
                error_serializer.is_valid(True)
                return Response(error_serializer.data)

        else:
            data = {'error': 'Must Provide Shop Id', 'status_code': 400}
            error_serializer = ErrorSerializer(data=data)
            error_serializer.is_valid(True)
            return Response(error_serializer.data)


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
                        data = {'error': 'Must Pass Valid Numbers', 'status_code': 400}
                        error_serializer = ErrorSerializer(data=data)
                        error_serializer.is_valid(True)
                        return Response(error_serializer.data)

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
                data = {'error': 'Shop does not exist', 'status_code': 400}
                error_serializer = ErrorSerializer(data=data)
                error_serializer.is_valid(True)
                return Response(error_serializer.data)

        else:
            data = {'error': 'Must Pass Shop Id', 'status_code': 400}
            error_serializer = ErrorSerializer(data=data)
            error_serializer.is_valid(True)
            return Response(error_serializer.data)


class ProductsValidatedView(APIView):

    def get(self, request, *args, **kwargs):
        if 'shop_id' in kwargs:
            shop_id = kwargs['shop_id']

            if Shop.objects.filter(pk=shop_id):
                db_products = Product.objects.filter(_shop_name=shop_id)
                product_ids = []
                for db_product in db_products:
                    link = db_product.link.replace("https://", "")
                    validation_link = http.client.HTTPSConnection(link)
                    try:
                        validation_link.request("GET", "")
                    except ImportError:
                        pass
                    response_link = validation_link.getresponse()
                    image_link = db_product.replace("https://", "")
                    validation_image_link = http.client.HTTPSConnection(image_link)
                    try:
                        validation_image_link.request("GET", "")
                    except ImportError:
                        pass
                    response_image_link = validation_image_link.getresponse()
                    if response_link.status == 200 or response_image_link.getresponse().status == 200:
                        product_ids.append(db_product.id)

                db_product = Shop.objects.filter(pk__in=product_ids)
                serializer = ProductSerializer(db_product, many=True)
                return Response(serializer.data)

            else:
                data = {'error': 'Product does not exist', 'status_code': 404}
                error_serializer = ErrorSerializer(data=data)
                error_serializer.is_valid(True)
                return Response(error_serializer.data)
        else:
            data = {'error': 'Must Pass Shop ID', 'status_code': 400}
            error_serializer = ErrorSerializer(data=data)
            error_serializer.is_valid(True)
            return Response(error_serializer.data)
