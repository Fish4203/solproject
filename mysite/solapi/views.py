from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
#from django.views import generic
from django.utils import timezone
from .models import *
from .generation import *
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
            'seed': system.seed,
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
            'seed': star.seed,
            'starClass': star.starClass,
            'mass': star.mass,
            'radius': star.radius,
            'temperature': star.temperature,

            'orbit': {
                'a': star.orbit.a,
                'b': star.orbit.b,
                'p': star.orbit.p,
                'period': star.orbit.period,
                'rotation': star.orbit.rotation,
                'bigM': star.orbit.bigM,
                'exentricity': star.orbit.exentricity
            }
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
            'seed': planet.seed,
            'planetType': planet.planetType,
            'mass': planet.mass,
            'radius': planet.radius,
            'gravity': planet.gravity,
            'tilt': planet.tilt,
            'axis': planet.axis,

            'atmosphere': {
                'presure': planet.atmosphere.presure,
                'nitrogen': planet.atmosphere.nitrogen,
                'oxygen': planet.atmosphere.oxygen,
                'argon': planet.atmosphere.argon,
                'carbonDioxide': planet.atmosphere.carbonDioxide,
                'neon': planet.atmosphere.neon,
                'helium': planet.atmosphere.helium,
                'methane': planet.atmosphere.methane,
                'sulpherDioxide': planet.atmosphere.sulpherDioxide,
                'hydrogen': planet.atmosphere.hydrogen,
                'sodium': planet.atmosphere.sodium,
                'potasium': planet.atmosphere.potasium,
            },

            'orbit': {
                'a': planet.orbit.a,
                'b': planet.orbit.b,
                'p': planet.orbit.p,
                'period': planet.orbit.period,
                'rotation': planet.orbit.rotation,
                'bigM': planet.orbit.bigM,
                'exentricity': planet.orbit.exentricity
            },

            'moons': [i.name for i in planet.moons.all()],
        }
    except:
        data = {
            'error': 'na'
        }


    return JsonResponse(data)

def generate(request, name, seed):

    systemGen(name, seed)

    return JsonResponse({'sucsess':True})
