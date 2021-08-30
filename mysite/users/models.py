import datetime
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.hashers import *
from django.utils import timezone
import random
import math
# Create your models here.




class Faction(models.Model):
    name = models.CharField(max_length=100)
    cash = models.IntegerField()
    description = models.CharField(max_length=500)
    stations = models.IntegerField() # placeholder

    factions = models.ManyToManyField('self', through='FactionFaction', symmetrical=False)

    def __str__(self):
        return self.name

class FactionFaction(models.Model):
    source = models.ForeignKey(Faction, on_delete=models.CASCADE, related_name='source')
    target = models.ForeignKey(Faction, on_delete=models.CASCADE, related_name='target')

    rep = models.IntegerField()
    status = models.CharField(max_length=100)


class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    cash = models.IntegerField()
    description = models.CharField(max_length=500)
    locSystem = models.CharField(max_length=100)

    locX = models.FloatField()
    locY = models.FloatField()
    locZ = models.FloatField()

    factions = models.ManyToManyField(Faction, through='PlayerFaction')

    def __str__(self):
        return self.name


class PlayerFaction(models.Model):
    faction = models.ForeignKey(Faction, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)

    rep = models.IntegerField()
    status = models.CharField(max_length=100)
