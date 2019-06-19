from django.test import TestCase
from api.models import Product, Shop


class ProductTestCase(TestCase):
    def setUp(self):
        shop = Shop.objects.create(title='Shop 1')
        Product.objects.create(shop_name=shop, title='Product 1',
                               link='https://www.visionarycph.com/products/sport-suede-cap-stone',
                               description='Sport cap made out of high quality faux suede. Adjustable metal buckle strap for custom fit. THIS CAP IS PART OF THE RAW COLLECTION.',
                               image_link='https://cdn.shopify.com/s/files/1/0739/8503/products/Sport_Suede_Cap_-_Stone_front.jpg?v=1459622281')

    def test_getter_id(self):
        product = Product.objects.get(_title='Product 1')
        self.assertEqual(product.id, 1)

    def test_getter_shop(self):
        shop = Shop.objects.get(_title='Shop 1')
        product = Product.objects.get(_title='Product 1')
        self.assertEqual(product.shop_name, shop)

    def test_getter_shop_id(self):
        product = Product.objects.get(_title='Product 1')
        self.assertEqual(product.shop_name.id, 1)

    def test_getter_title(self):
        product = Product.objects.get(_title='Product 1')
        self.assertEqual(product.title, 'Product 1')

    def test_getter_link(self):
        product = Product.objects.get(_title='Product 1')
        self.assertEqual(product.link, 'Some link')

    def test_getter_description(self):
        product = Product.objects.get(_title='Product 1')
        self.assertEqual(product.description, 'Some description')

    def test_getter_image_link(self):
        product = Product.objects.get(_title='Product 1')
        self.assertEqual(product.image_link, 'Some image link')
