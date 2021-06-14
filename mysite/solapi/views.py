from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
#from django.views import generic
from django.utils import timezone
from .models import *
# Create your views here.


def info(request):
    data = {
        'test': True
    }
    return JsonResponse(data)

def getSystem(request, systemName):

    try:
        system = System.objects.get(name=str(systemName))

        data = {
            'name': system.name,
            'stars': [i.name for i in system.stars.all()],
            'planets': [i.name for i in system.planets.all()],
        }
    except:
        data = {
            'error': 'na'
        }


    return JsonResponse(data)

def getStar(request, starName):

    try:
        star = Star.objects.get(name=starName)
        data = {
            'name': star.name,
            'sunType': star.sunType,
            'mass': star.mass,
            'radius': star.radius,
            'temp': star.temp,
            'orbit': star.orbit,
            'orbitRadius': star.orbitRadius,
        }
    except:
        data = {
            'error': 'na'
        }


    return JsonResponse(data)

def getPlanet(request, planetName):

    try:
        planet = Planet.objects.get(name=planetName)

        data = {
            'name': planet.name,
            'sunType': planet.sunType,
            'mass': planet.mass,
            'radius': planet.radius,
            'temp': planet.temp,
            'atmos': planet.atmos,
            'seed': planet.seed,
            'rSpeed': planet.rSpeed,
            'orbit': planet.orbit,
            'orbitRadius': planet.orbitRadius,
        }
    except:
        data = {
            'error': 'na'
        }


    return JsonResponse(data)

def generate(request, name):

    data = {}

    return JsonResponse(data)
