import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random
import math
from shipdata.models import *
from solapi.models import *
# Create your models here.

class FactionRep(models.Model):
    rep = models.IntegerField()
    status = models.CharField(max_length=100)


class Faction(models.Model):
    name = models.CharField(max_length=100)
    cash = models.IntegerField()
    description = models.CharField(max_length=500)
    stations = models.IntegerField() # placeholder

    factions = models.ManyToManyField(FactionRep)

    players = models.ManyToManyField(FactionRep)

class Player(models.Model):
    name = models.CharField(max_length=100)
    cash = models.IntegerField()
    description = models.CharField(max_length=500)
    locSystem = models.CharField(max_length=100)
    locX = models.FloatField()
    locY = models.FloatField()
    locZ = models.FloatField()

    factions = models.ManyToManyField(FactionRep)

    def __str__(self):
        return self.name
