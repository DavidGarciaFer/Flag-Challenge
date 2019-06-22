from __future__ import unicode_literals

from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

class Record(models.Model):
    player = models.ForeignKey(Player)
    points = models.IntegerField(default=0)
    date = models.DateField()

    def __str__(self):
        return self.player.name + ': ' + str(self.points)
    
    def __unicode__(self):
        return self.player.name + ': ' + str(self.points)