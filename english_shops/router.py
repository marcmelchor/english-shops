from api.views import ShopViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('shop', ShopViewSet, base_name='Shop')
