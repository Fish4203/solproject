import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from jsonfield import JSONField
# Create your models here.

class Star(models.Model):
    name = models.CharField(max_length=100)
    sunType = models.CharField(max_length=100)
    mass = models.IntegerField()
    radius = models.IntegerField()
    temp = models.IntegerField()
    orbit = models.CharField(max_length=100)
    orbitRadius = models.IntegerField()

    def __str__(self):
        return self.name

class Planet(models.Model):
    name = models.CharField(max_length=100)
    planetType = models.CharField(max_length=100)
    mass = models.IntegerField()
    radius = models.IntegerField()
    temp = models.IntegerField()
    atmos = models.IntegerField()
    seed = models.IntegerField()
    rSpeed = models.IntegerField()
    orbit = models.CharField(max_length=100)
    orbitRadius = models.IntegerField()

    moons = models.ManyToManyField('self')

    def __str__(self):
        return self.name

class System(models.Model):
    name = models.CharField(max_length=100)
    stars = models.ManyToManyField(Star)
    planets = models.ManyToManyField(Planet)
    #ast = models.ManyToManyField(Ast)

    def __str__(self):
        return self.name
