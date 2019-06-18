from api.views import ShopViewSet, ProductViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('shop', ShopViewSet, base_name='Shop')
router.register('product', ProductViewSet, base_name='Product')
