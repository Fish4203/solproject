import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random
import math
from users.models import *
from shipdata.models import *
# Create your models here.

class Element(models.Model):
    name = models.CharField(max_length=100)
    stable = models.IntegerField()
    # other verables tba

    def __str__(self):
        return self.name

class Atmosphere(models.Model):

    presure = models.FloatField() # presure of the atmosphere Units: KPa

    # all the rest are in percentages
    elemants = models.ManyToManyField(Element)

class Orbit(models.Model):
    # orbit shit
    # https://www.desmos.com/calculator/xr6lrvad5a

    a = models.FloatField() # semi major axis of the elipse Units: AU
    exentricity = models.FloatField() # the ecentricity what do you want a phisics lession
    b = models.FloatField() # semi minor axis of the elipse Units: AU
    p = models.FloatField() # idk what this means
    period = models.FloatField() # ok now this one is ovious Units: seconds
    rotation = models.FloatField() # the rotation of the orbit around the center Units: deg
    bigM = models.FloatField() # the mass of the larger object Units: KG

class Star(models.Model):
    name = models.CharField(max_length=100)
    seed = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    starClass = models.CharField(max_length=100)
    mass = models.FloatField() # mass of the star  Units: kg
    radius = models.FloatField() # radius of the star Units: AU
    temperature = models.FloatField() # trmprature Units: kg

    orbit = models.OneToOneField(Orbit, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class Planet(models.Model):
    name = models.CharField(max_length=100) # the name of the planet
    seed = models.CharField(max_length=100) # the random seed
    description = models.CharField(max_length=500)
    planetType = models.CharField(max_length=100) # ice or gas or rock
    mass = models.FloatField() # the mass of the planet Units: kg
    radius = models.FloatField() # radius of the planet Units: AU
    gravity = models.FloatField() # gravity or little g Units: kgms^2 i think
    tilt = models.FloatField() # the tilt the planet of the spin from the sun Units: deg
    axis = models.FloatField() # the tilt of the orbetal plane Units: deg

    elemants = models.ManyToManyField(Element)
    atmosphere = models.OneToOneField(Atmosphere, on_delete=models.CASCADE)
    orbit = models.OneToOneField(Orbit, on_delete=models.CASCADE)

    moons = models.ManyToManyField('self')

    def __str__(self):
        return self.name


class Asteroid(models.Model):
    name = models.CharField(max_length=100)
    seed = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    type = models.CharField(max_length=100)

    # richness
    l = models.FloatField() # -10 to 10
    k = models.FloatField() # -1 to 1

    elemants = models.ManyToManyField(Element)
    orbit = models.OneToOneField(Orbit, on_delete=models.CASCADE)



class System(models.Model):
    name = models.CharField(max_length=100)
    seed = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    stars = models.ManyToManyField(Star)
    planets = models.ManyToManyField(Planet)
    asteroids = models.ManyToManyField(Asteroid)

    locX = models.FloatField()
    locY = models.FloatField()
    locZ = models.FloatField()

    def __str__(self):
        return self.name
