import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random
import math
from users.models import *
from solapi.models import *
# Create your models here.

class Reactor(models.Model):
    type = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    repairness = models.IntegerField()
    maxTemp = models.IntegerField()
    minTemp = models.IntegerField()

    mean = models.FloatField()
    stdev = models.FloatField()

class HyperDrive(models.Model):
    type = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    repairness = models.IntegerField()
    maxTemp = models.IntegerField()
    minTemp = models.IntegerField()

    mean = models.FloatField()
    stdev = models.FloatField()

class Thruster(models.Model):
    type = models.CharField(max_length=100)
    size = models.IntegerField()
    designer = models.CharField(max_length=100)
    repairness = models.IntegerField()
    maxTemp = models.IntegerField()
    minTemp = models.IntegerField()

    mean = models.FloatField()
    stdev = models.FloatField()
    power = models.FloatField()
    overload = models.IntegerField()

class PowerBank(models.Model):
    type = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    repairness = models.IntegerField()
    maxTemp = models.IntegerField()
    minTemp = models.IntegerField()

    mean = models.FloatField()
    stdev = models.FloatField()
    capacity = models.FloatField()

class LifeSupport(models.Model):
    type = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    repairness = models.IntegerField()
    maxTemp = models.IntegerField()
    minTemp = models.IntegerField()

    o2Capacity = models.FloatField()
    power = models.FloatField()
    co2reprocesing = models.FloatField()
    tempcontrol = models.IntegerField()

class Repulsion(models.Model):
    type = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    repairness = models.IntegerField()
    maxTemp = models.IntegerField()
    minTemp = models.IntegerField()

    strength = models.IntegerField()
    charge = models.FloatField()
    disRate = models.FloatField()
    chRate = models.FloatField()

class Fuel(models.Model):
    type = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    repairness = models.IntegerField()
    maxTemp = models.IntegerField()
    minTemp = models.IntegerField()

    capacity = models.FloatField()
    power = models.FloatField()

class Hull(models.Model):
    type = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    repairness = models.IntegerField()
    maxTemp = models.IntegerField()
    minTemp = models.IntegerField()

    passiveHeat = models.FloatField()
    activeHeat = models.FloatField()
    hp = models.FloatField()

class Weapon(models.Model):
    type = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    repairness = models.IntegerField()
    maxTemp = models.IntegerField()
    minTemp = models.IntegerField()

    damageK = models.FloatField()
    damageH = models.FloatField()
    damageE = models.FloatField()
    power = models.FloatField()
    ammoType = models.CharField(max_length=100)

class Computer(models.Model):
    type = models.CharField(max_length=100)
    designer = models.CharField(max_length=100)
    repairness = models.IntegerField()
    maxTemp = models.IntegerField()
    minTemp = models.IntegerField()

    power = models.FloatField()
    sensorRange = models.FloatField()

class Ship(models.Model):
    name = models.CharField(max_length=100)
    owner = models.OneToOneField(Player, on_delete=models.CASCADE)
    designer = models.CharField(max_length=100)
    shipType = models.CharField(max_length=100)

    # components
    reactors = models.ManyToManyField(Reactor)
    hyperDrives = models.ManyToManyField(HyperDrive)
    thrusters = models.ManyToManyField(Thruster)
    powerBanks = models.ManyToManyField(PowerBank)
    lifeSupports = models.ManyToManyField(LifeSupport)
    repulsions = models.ManyToManyField(Repulsion)
    fuels = models.ManyToManyField(Fuel)
    hulls = models.ManyToManyField(Hull)
    weapons = models.ManyToManyField(Weapon)
    computers = models.ManyToManyField(Computer)

    locSystem = models.CharField(max_length=100)
    locX = models.FloatField()
    locY = models.FloatField()
    locZ = models.FloatField()



    def __str__(self):
        return self.name
