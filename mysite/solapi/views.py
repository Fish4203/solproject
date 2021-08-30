from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
#from django.views import generic
from django.utils import timezone
from .models import *
from .generation import *
from django.core.serializers.json import DjangoJSONEncoder
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.core.serializers import serialize

# Create your views here.

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Planet):
            return 'str(obj)'
        return super().default(obj)



class SystemView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', System.objects.filter(id=pk), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find system'}
            else:
                data = data[0]

            data['fields']['planets'] = serialize('python', System.objects.get(id=pk).planets.all(), cls=LazyEncoder)

        except:
            data = {'status': 'error geting data'}

        return JsonResponse(data)

    def patch(self, request, pk):
        try:
            system = System.objects.get(id=pk)

            if len(system.stars.all()) != 0:
                return JsonResponse({'status': 'already exists'})

            random.seed(system.seed)

            star = starGen(name= name+'star'+'a', seed=str(random.random()))
            system.stars.add(star)

            bigM = star.mass

            for i in range(0, random.randint(0,10)):
                # how many planets are going to be gened
                system.planets.add(planetGen(name=name+'planet'+str(i), seed=str(random.random()), bigM=bigM))

            system.save()

            return JsonResponse({'status': 'sucsess'})


        except:
            return JsonResponse({'status': 'cant update system'})

class PlanetView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', Planet.objects.filter(id=pk), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find planet'}
            else:
                data = data[0]

        except:
            data = {'status': 'error geting data'}

        return JsonResponse(data)

class AsteroidView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', Asteroid.objects.filter(id=pk), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find asteroid'}
            else:
                data = data[0]

        except:
            data = {'status': 'error geting data'}

        return JsonResponse(data)

class StarView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', Star.objects.filter(id=pk), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find star'}
            else:
                data = data[0]

        except:
            data = {'status': 'error geting data'}

        return JsonResponse(data)


def info(request):
    data = {
        'test': True
    }
    return JsonResponse(data)
