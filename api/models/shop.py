from django.db import models


class Shop(models.Model):
    _title = models.CharField(max_length=100, blank=True, default='')

    def __str__(self):
        return self._title

    def __unicode__(self):
        return '/%s/' % self._title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value='default'):
        if value is not None:
            self._title = value[: 100]
