import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import random
import math
# Create your models here.

class Star(models.Model):
    name = models.CharField(max_length=100)
    starClass = models.CharField(max_length=100)
    mass = models.IntegerField()
    radius = models.IntegerField()
    temperature = models.IntegerField()
    orbit = models.CharField(max_length=100)
    orbitRadius = models.IntegerField()
    seed = models.IntegerField()

    def __str__(self):
        return self.name

    def generate(self, name):
        self.name = name
        random.seed = self.seed

        t_val = random.random()  # Temp variable

        if t_val <= 0.0000003:
            self.starClass = 'O'
            self.mass = random.randrange(160000, 320000)  # *10^26 kilograms
            self.radius = self.mass * 0.4125  # In Solar radii (6.975*10^5km)
            self.temperature = math.floor(4*math.pi*self.radius*self.radius * 42.6264386916 + 6666.67)  # Kelvin (many thousands) The area of the sun multiplies by the gradient of the relationship between area and termperate for its class
        elif 0.0000003 < t_val <= 0.0013003:
            self.starClass = 'B'
            self.mass = random.randrange(21000, 160000)  # *10^26 kilograms
            self.radius = self.mass * 0.345323741007 + 1.47842  # In Solar radii (6.975*10^5km)
            self.temperature = math.floor(4*math.pi*self.radius*self.radius * 39.4729521557 + 8392.86)
        elif 0.0013003 < t_val <= 0.0073003:
            self.starClass = 'A'
            self.mass = random.randrange(14000, 21000)  # *10^26 kilograms
            self.radius = self.mass * 0.571428571429 + 0.6  # In Solar radii (6.975*10^5km)
            self.temperature = math.floor(4*math.pi*self.radius*self.radius * 155.424749113 + 3671.88)
        elif 0.0073003 < t_val <= 0.0373003:
            self.starClass = 'F'
            self.mass = random.randrange(10400, 14000)  # *10^26 kilograms
            self.radius = self.mass * 0.694444444444 + 1.58333  # In Solar radii (6.975*10^5km)
            self.temperature = math.floor(4*math.pi*self.radius*self.radius * 187.24110952 + 2888.24)
        elif 0.0373003 < t_val <= 0.1133:
            self.starClass = 'G'
            self.mass = random.randrange(8000, 10400)  # *10^26 kilograms
            self.radius = self.mass * 0.791666666667 + 0.326667  # In Solar radii (6.975*10^5km)
            self.temperature = math.floor(4*math.pi*self.radius*self.radius * 158.797648383 + 3360.94)
        elif 0.1133 < t_val <= 0.2343:
            self.starClass = 'K'
            self.mass = random.randrange(4500, 8000)  # *10^26 kilograms
            self.radius = self.mass * 1.34615384615 + 0.365714  # In Solar radii (6.975*10^5km)
            self.temperature = math.floor(4*math.pi*self.radius*self.radius * 276.56674541 + 1997.03)
        else:
            self.starClass = 'M'
            self.mass = random.randrange(800, 4500)  # *10^26 kilograms
            self.radius = self.mass * 1.75675675676 + -0.77973  # In Solar radii (6.975*10^5km)
            self.temperature = math.floor(4*math.pi*self.radius*self.radius * 212.206590789 + 2393.33)

        self.orbit = '0'
        self.orbitRadius = 0


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
