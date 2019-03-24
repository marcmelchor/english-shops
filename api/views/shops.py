from api.models import Shop
from rest_framework.views import APIView
from rest_framework.response import Response
from api.resources.serializers import ShopSerializer, ErrorSerializer


class ShopView(APIView):

    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def get(self, request, *args, **kwargs):
        if 'shop_id' in kwargs:
            shop_id = kwargs['shop_id']

            if Shop.objects.filter(pk=shop_id):
                db_shop = Shop.objects.get(pk=shop_id)
                serializer = ShopSerializer(db_shop)
                return Response(serializer.data)
            else:
                data = {'error': 'Shop does not exist', 'status_code': 404}
                error_serializer = ErrorSerializer(data=data)
                error_serializer.is_valid(True)
                return Response(error_serializer.data)
        else:
            is_limited = False
            start = request.GET.get('start', None)
            end = request.GET.get('end', None)
            if start and end:
                if not start.isnumeric() or not end.isnumeric():
                    data = {'error': 'Must Pass Valid Numbers', 'status_code': 404}
                    error_serializer = ErrorSerializer(data=data)
                    error_serializer.is_valid(True)
                    return Response(error_serializer.data)

                start_nun = int(start)
                end_num = int(end)
                is_limited = True

            if is_limited:
                db_shop = Shop.objects.all()[start_nun: end_num]
                serializer = ShopSerializer(db_shop, many=True)
                return Response(serializer.data)
            else:
                db_shop = Shop.objects.all()
                serializer = ShopSerializer(db_shop, many=True)
                return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        shop = request.data.get('shop')
        serializer = ShopSerializer(data=shop)
        if serializer.is_valid(raise_exception=True):
            shop_saved = Shop()
            shop_saved.title = shop["title"]
            shop_saved.save()

            return Response({"Success": "Shop '{}' created successfully".format(shop_saved.title)})

        else:
            data = {'error': 'Error Creating Shop', 'status_code': 400}
            error_serializer = ErrorSerializer(data=data)
            error_serializer.is_valid(True)
            return Response(error_serializer.data)

    def delete(self, request, *args, **kwargs):

        if 'shop_id' in kwargs:
            shop_id = kwargs['shop_id']

            if Shop.objects.filter(pk=shop_id):
                db_shop = Shop.objects.get(pk=shop_id)
                title = db_shop.title
                Shop.objects.get(pk=shop_id).delete()
                return Response({"Success": "Shop '{}' deleted successfully".format(title)})

            else:
                data = {'error': 'Shop does not exist', 'status_code': 400}
                error_serializer = ErrorSerializer(data=data)
                error_serializer.is_valid(True)
                return Response(error_serializer.data)

        else:
            data = {'error': 'Must pass shop id', 'status_code': 400}
            error_serializer = ErrorSerializer(data=data)
            error_serializer.is_valid(True)
            return Response(error_serializer.data)
