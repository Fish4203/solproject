import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random
import math
# Create your models here.

class Componet(models.Model):
    name = models.CharField(max_length=100)
    faction = models.OneToOneField(Faction, on_delete=models.CASCADE)


class ShipType(models.Model):
    name = models.CharField(max_length=100)
    faction = models.OneToOneField(Faction, on_delete=models.CASCADE)



class Ship(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(Player, on_delete=models.CASCADE)

    shipType =


    locSystem = models.CharField(max_length=100)
    locX = models.FloatField()
    locY = models.FloatField()
    locZ = models.FloatField()



    def __str__(self):
        return self.name
