from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import *
# Create your views here.


def newUser(request):
    if request.method == 'POST':
        try:
            user = User.objects.create_user(username=request.POST['username'], email=request.POST['email'], password=request.POST['password'])
            user.save()

            player = Player(user=user, name=request.POST['username'], cash=0, description='', locSystem='', locX=0,locY=0,locZ=0)
            player.save()

            return render(request, 'user/newUser.html', {'message': 'New acount created'})
        except:
            return render(request, 'user/newUser.html', {'message': 'Failed to make account'})
    else:
        return render(request, 'user/newUser.html')

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)



# def getPlayer(request, playerName):
#
#     try:
#         player = Player.objects.get(name=str(playerName))
#
#         data = {
#             'name': player.name,
#             'cash': player.cash,
#             'factions': [i.faction_set.all()[0].name : {'cash': i.faction_set.all()[0].cash, 'stations': i.faction_set.all()[0].stations, 'rep': i.status, 'status': i.rep} for i in player.factions.all()],
#         }
#     except:
#         data = {
#             'error': 'na'
#         }
#
#
#     return JsonResponse(data)
#
# def getFaction(request, FactionName):
#
#     try:
#         faction = Faction.objects.get(name=FactionName)
#         data = {
#             'name': faction.name,
#             'cash': faction.cash,
#             'factions': [i.faction_set.all().exclude(name=faction.name)[0].name : {'cash': i.faction_set.all().exclude(name=faction.name)[0].cash, 'stations': i.faction_set.all().exclude(name=faction.name)[0].faction_set.all()[0].stations, 'rep': i.status, 'status': i.rep} for i in faction.factions.all()],
#             'player': [i.player_set.all()[0].name : {'cash': i.player_set.all()[0].cash, 'stations': i.player_set.all()[0].stations, 'rep': i.status, 'status': i.rep} for i in faction.players.all()],
#         }
#     except:
#         data = {
#             'error': 'na'
#         }
#
#
#     return JsonResponse(data)
