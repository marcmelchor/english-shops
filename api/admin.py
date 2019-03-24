from django.contrib import admin
from .models import Shop, Product


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', '_title')
    search_fields = ('_title',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', '_title', '_shop_name')
    search_fields = ('_title', '_description', '_shop_name')


admin.site.register(Shop, ShopAdmin)
admin.site.register(Product, ProductAdmin)
