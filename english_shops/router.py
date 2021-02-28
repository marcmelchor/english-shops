from api.views import ShopViewSet, ProductViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('shop', ShopViewSet, basename='Shop')
router.register('product', ProductViewSet, basename='Product')
