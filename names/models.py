from __future__ import unicode_literals

from django.db import models

class Country(models.Model):
    name_en = models.CharField(max_length=128)
    name_es = models.CharField(max_length=128)
    name_fr = models.CharField(max_length=128)
    iso2 = models.CharField(max_length=2, unique=True)
    iso3 = models.CharField(max_length=3, unique=True)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name_es

    def __unicode__(self):
        return self.name_es
