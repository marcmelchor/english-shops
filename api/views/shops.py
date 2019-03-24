from api.models import Shop
from rest_framework.views import APIView
from rest_framework.response import Response
from api.resources.serializers import ShopSerializer, ShopJSON


class ShopView(APIView):

    def get(self, request, *args, **kwargs):
        if 'shop_id' in kwargs:
            shop_id = kwargs['shop_id']

            if Shop.objects.filter(pk=shop_id):
                db_shop = Shop.objects.get(pk=shop_id)
                serializer = ShopSerializer(db_shop)
                return Response(serializer.data)
            else:
                return Response('Shop does not exist')
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
                db_shop = Shop.objects.all()[start_nun: end_num]
                serializer = ShopSerializer(db_shop, many=True)
                return Response(serializer.data)
            else:
                db_shop = Shop.objects.all()
                serializer = ShopJSON.get_json_shop(db_shop)
                # serializer = ShopSerializer(db_shop, many=True)
                return Response(serializer)

    def post(self, request, *args, **kwargs):
        pass
