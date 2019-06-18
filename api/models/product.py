from django.db import models
from api.models import Shop


class Product(models.Model):
    _shop_name = models.ForeignKey(Shop, on_delete=models.SET_NULL, null=True)
    _title = models.CharField(max_length=100, blank=True, default='')
    _link = models.CharField(max_length=100, blank=True, default='')
    _description = models.CharField(max_length=500, blank=True, default='')
    _image_link = models.CharField(max_length=200, blank=True, default='')

    def __str__(self):
        return self._title

    def __unicode__(self):
        return '/%s/' % self._title

    @property
    def shop_name(self):
        return self._shop_name

    @shop_name.setter
    def shop_name(self, value):
        self._shop_name = value

    @property
    def shop_name_id(self):
        return self._shop_name_id

    @shop_name_id.setter
    def shop_name_id(self, value):
        self._shop_name_id = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value=''):
        if value is not None:
            self._title = value[: 100]

    @property
    def link(self):
        return self._link

    @link.setter
    def link(self, value=''):
        if value is not None:
            self._link = value[: 100]

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value=''):
        if value is not None:
            self._description = value[: 500]

    @property
    def image_link(self):
        return self._image_link

    @image_link.setter
    def image_link(self, value=''):
        if value is not None:
            self._image_link = value[: 200]
