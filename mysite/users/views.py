from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.utils import timezone
from .models import *
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize
from django.db.models import Q
# Create your views here.

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, YourCustomType):
            return str(obj)
        return super().default(obj)



class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            data = serialize('python', Player.objects.filter(name=request.user.username), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find system'}
            else:
                data = data[0]

        except:
            data = {'status': 'error geting data'}

        return JsonResponse(data)

class UserFactionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        try:
            data = {'factions': serialize('python', PlayerFaction.objects.filter(player=Player.objects.filter(name=request.user.username)[0]), cls=LazyEncoder)}

        except:
            data = {'status': 'error geting data'}

        return JsonResponse(data)

class FactionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', Faction.objects.filter(id=pk), cls=LazyEncoder)[0]
        except:
            data = {'status': 'error geting data'}

        return JsonResponse(data)

class FactionFactionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = {'factions': serialize('python', FactionFaction.objects.filter(Q(source=Faction.objects.filter(id=pk)[0]) | Q(target=Faction.objects.filter(id=pk)[0])), cls=LazyEncoder)}

        except:
            data = {'status': 'error geting data'}

        return JsonResponse(data)

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
