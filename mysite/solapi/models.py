import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random
import math
# Create your models here.

class Atmosphere(models.Model):

    presure = models.FloatField() # presure of the atmosphere Units: KPa

    # all the rest are in percentages
    nitrogen = models.FloatField()
    oxygen = models.FloatField()
    argon = models.FloatField()
    carbonDioxide = models.FloatField()
    neon = models.FloatField()
    helium = models.FloatField()
    methane = models.FloatField()
    sulpherDioxide = models.FloatField()
    hydrogen = models.FloatField()
    sodium = models.FloatField()
    potasium = models.FloatField()

class Orbit(models.Model):
    # orbit shit
    # https://www.desmos.com/calculator/xr6lrvad5a

    a = models.FloatField() # semi major axis of the elipse Units: AU
    b = models.FloatField() # semi minor axis of the elipse Units: AU
    rotation = models.FloatField() # the rotation of the orbit around the center Units: deg
    bigM = models.FloatField() # the mass of the larger object Units: KG

class Star(models.Model):
    name = models.CharField(max_length=100)
    seed = models.CharField(max_length=100)
    starClass = models.CharField(max_length=100)
    mass = models.IntegerField()
    radius = models.IntegerField()
    temperature = models.IntegerField()

    orbit = models.OneToOneField(Orbit, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Planet(models.Model):
    name = models.CharField(max_length=100)
    seed = models.CharField(max_length=100)
    planetType = models.CharField(max_length=100)
    mass = models.IntegerField()
    radius = models.IntegerField()
    gravity = models.IntegerField()
    tilt = models.IntegerField()
    axis = models.IntegerField()

    atmosphere = models.OneToOneField(Atmosphere, on_delete=models.CASCADE)
    orbit = models.OneToOneField(Orbit, on_delete=models.CASCADE)

    moons = models.ManyToManyField('self')

    def __str__(self):
        return self.name



class System(models.Model):
    name = models.CharField(max_length=100)
    seed = models.CharField(max_length=100)
    stars = models.ManyToManyField(Star)
    planets = models.ManyToManyField(Planet)
    #ast = models.ManyToManyField(Ast)

    orbit = models.OneToOneField(Orbit, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
