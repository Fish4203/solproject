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

def getPlayer(request, playerName):

    try:
        player = Player.objects.get(name=str(playerName))

        data = {
            'name': player.name,
            'cash': player.cash,
            'factions': [i.faction_set.all()[0].name : {'cash': i.faction_set.all()[0].cash, 'stations': i.faction_set.all()[0].stations, 'rep': i.status, 'status': i.rep} for i in player.factions.all()],
        }
    except:
        data = {
            'error': 'na'
        }


    return JsonResponse(data)

def getFaction(request, FactionName):

    try:
        faction = Faction.objects.get(name=FactionName)
        data = {
            'name': faction.name,
            'cash': faction.cash,
            'factions': [i.faction_set.all().exclude(name=faction.name)[0].name : {'cash': i.faction_set.all().exclude(name=faction.name)[0].cash, 'stations': i.faction_set.all().exclude(name=faction.name)[0].faction_set.all()[0].stations, 'rep': i.status, 'status': i.rep} for i in faction.factions.all()],
            'player': [i.player_set.all()[0].name : {'cash': i.player_set.all()[0].cash, 'stations': i.player_set.all()[0].stations, 'rep': i.status, 'status': i.rep} for i in faction.players.all()],
        }
    except:
        data = {
            'error': 'na'
        }


    return JsonResponse(data)
