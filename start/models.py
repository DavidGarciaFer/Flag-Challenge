from __future__ import unicode_literals

from django.db import models

class Country(models.Model):
    c_id = models.CharField()
    name_en = models.CharField(max_length=128)
    name_es = models.CharField(max_length=128)
    name_fr = models.CharField(max_length=128)
    iso2 = models.CharField(max_length=2)
    iso3 = models.CharField(max_length=3)

    def __str__(self):
        return self.iso2

    def __unicode__(self):
        return self.iso2