from api.models import Product, Shop
from rest_framework.views import APIView
from rest_framework.response import Response
import json
from django.conf import settings


class PopulateDBView(APIView):

    def get(self, request, *args, **kwargs):

        if not Product.objects.all() or not Product.objects.all():
            with open(settings.JSON_FILE) as f:
                dict_data = json.load(f)
                str_data = json.dumps(dict_data, ensure_ascii=False)
                shop_names = []
                # Get the first shop
                first_split = str_data.split('{"')
                second_split = first_split[1].split('": [')
                first_shop = second_split[0]
                shop_names.append(first_shop)
                # Loop to get all the shop names and save to the database
                shops_split = str_data.split('"}], "')
                for shop in shops_split:
                    head, sep, tail = shop.partition('"')
                    if len(head) > 2:
                        shop_names.append(head)

                for shop_name in shop_names:
                    shop_db = Shop()
                    shop_db.title = shop_name
                    shop_db.save()
                    print('Shop saved: ' + str(shop_db.title))
                    for product in dict_data[shop_name]:
                        product_db = Product()
                        product_db.shop_name = shop_db
                        product_db.title = product['title']
                        product_db.link = product['link']
                        product_db.description = product['description']
                        product_db.image_link = product['image_link']
                        product_db.save()
                        print('Product saved: ' + str(product_db.title))

            return Response('Database migrated')

        else:
            return Response('Error')
