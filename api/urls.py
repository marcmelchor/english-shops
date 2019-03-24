from django.urls import path
from api.views.shops import ShopView
from api.views.products import ProductView, ProductsInShopView, ProductsValidatedView
from api.views.populate_db import PopulateDBView

urlpatterns = [
    path('shops/', ShopView.as_view(), name='shops'),
    path('shops/<int:shop_id>/', ShopView.as_view(), name='shop'),
    path('shops/<int:shop_id>/products/', ProductsInShopView.as_view(), name='Products in shop'),
    path('shops/<int:shop_id>/validated_validated/', ProductsValidatedView.as_view(), name='Validated Products'),
    path('products/', ProductView.as_view(), name='products'),
    path('products/<int:product_id>/', ProductView.as_view(), name='product'),
    path('products_validated/<int:product_id>/', ProductView.as_view(), name='product validated'),
    path('populate_db/', PopulateDBView.as_view(), name='populate'),
]
