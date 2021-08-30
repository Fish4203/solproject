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



class ShipView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', Ship.objects.filter(id=pk), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find system'}
            else:
                data = data[0]

            data['fields']['reactors'] = serialize('python', System.objects.get(id=pk).reactors.all(), cls=LazyEncoder)
            data['fields']['hyperDrives'] = serialize('python', System.objects.get(id=pk).hyperDrives.all(), cls=LazyEncoder)
            data['fields']['thrusters'] = serialize('python', System.objects.get(id=pk).thrusters.all(), cls=LazyEncoder)
            data['fields']['powerBanks'] = serialize('python', System.objects.get(id=pk).powerBanks.all(), cls=LazyEncoder)
            data['fields']['lifeSupports'] = serialize('python', System.objects.get(id=pk).lifeSupports.all(), cls=LazyEncoder)
            data['fields']['repulsions'] = serialize('python', System.objects.get(id=pk).repulsions.all(), cls=LazyEncoder)
            data['fields']['fuels'] = serialize('python', System.objects.get(id=pk).fuels.all(), cls=LazyEncoder)
            data['fields']['hulls'] = serialize('python', System.objects.get(id=pk).hulls.all(), cls=LazyEncoder)
            data['fields']['weapons'] = serialize('python', System.objects.get(id=pk).weapons.all(), cls=LazyEncoder)
            data['fields']['computers'] = serialize('python', System.objects.get(id=pk).computers.all(), cls=LazyEncoder)
        except:
            data = {'status': 'error geting data'}
        return JsonResponse(data)

class ReactorView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', Reactor.objects.filter(id=pk), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find system'}
            else:
                data = data[0]
        except:
            data = {'status': 'error geting data'}
        return JsonResponse(data)

class HyperDriveView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', HyperDrive.objects.filter(id=pk), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find system'}
            else:
                data = data[0]
        except:
            data = {'status': 'error geting data'}
        return JsonResponse(data)

class ThrusterView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', Thruster.objects.filter(id=pk), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find system'}
            else:
                data = data[0]
        except:
            data = {'status': 'error geting data'}
        return JsonResponse(data)

class PowerBankView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', PowerBank.objects.filter(id=pk), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find system'}
            else:
                data = data[0]
        except:
            data = {'status': 'error geting data'}
        return JsonResponse(data)

class LifeSupportView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', LifeSupport.objects.filter(id=pk), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find system'}
            else:
                data = data[0]
        except:
            data = {'status': 'error geting data'}
        return JsonResponse(data)

class RepulsionView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', Repulsion.objects.filter(id=pk), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find system'}
            else:
                data = data[0]
        except:
            data = {'status': 'error geting data'}
        return JsonResponse(data)

class FuelView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', Fuel.objects.filter(id=pk), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find system'}
            else:
                data = data[0]
        except:
            data = {'status': 'error geting data'}
        return JsonResponse(data)

class HullView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', Hull.objects.filter(id=pk), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find system'}
            else:
                data = data[0]
        except:
            data = {'status': 'error geting data'}
        return JsonResponse(data)

class WeaponView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', Weapon.objects.filter(id=pk), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find system'}
            else:
                data = data[0]
        except:
            data = {'status': 'error geting data'}
        return JsonResponse(data)

class ComputerView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        try:
            data = serialize('python', Computer.objects.filter(id=pk), cls=LazyEncoder)

            if len(data) != 1:
                data = {'status': 'cant find system'}
            else:
                data = data[0]
        except:
            data = {'status': 'error geting data'}
        return JsonResponse(data)
