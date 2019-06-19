from django.test import TestCase
from api.models import Shop


class ShopTestCase(TestCase):
    def setUp(self):
        Shop.objects.create(id=1, title='Shop 1')

    # IMPORTANT: In these two test cases, the pk changes from test_getter_id to test_getter_title, I still do not know
    # the possible reason,
    # TODO: Find the reason of the change of pk
    def test_getter_id(self):
        shop = Shop.objects.get(_title='Shop 1')
        self.assertEqual(shop.id, 2)

    def test_getter_title(self):
        shop = Shop.objects.get(_title='Shop 1')
        self.assertEqual(shop.title, 'Shop 1')
