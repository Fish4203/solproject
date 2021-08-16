import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random
import math
from users.models import *
from solapi.models import *
# Create your models here.

class Item(models.Model):
    name = models.CharField(max_length=100)
    stable =  models.IntegerField()

    # more info needed
    def __str__(self):
        return self.name

class Componet(models.Model):
    name = models.CharField(max_length=100)
    faction = models.OneToOneField(Faction, on_delete=models.CASCADE)

    # more info needed
    def __str__(self):
        return self.name

class ShipType(models.Model):
    name = models.CharField(max_length=100)
    faction = models.OneToOneField(Faction, on_delete=models.CASCADE)

    # more info needed
    def __str__(self):
        return self.name

class Ship(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(Player, on_delete=models.CASCADE)

    # more info needed
    shipType = models.ForeignKey(ShipType)


    locSystem = models.CharField(max_length=100)
    locX = models.FloatField()
    locY = models.FloatField()
    locZ = models.FloatField()



    def __str__(self):
        return self.name

class Ship(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(Player, on_delete=models.CASCADE)

    # more info needed
    shipType = models.ForeignKey(ShipType)


    locSystem = models.CharField(max_length=100)
    locX = models.FloatField()
    locY = models.FloatField()
    locZ = models.FloatField()



    def __str__(self):
        return self.name
