from django.urls import path
from . import views

app_name = 'solapi'
urlpatterns = [
    path('', views.info, name='info'),
    path('getSystem/<str:systemName>', views.getSystem, name='getSystem'),
    path('getStar/<str:starName>', views.getStar, name='getStar'),
    path('getPlanet/<str:planetName>', views.getPlanet, name='getPlanet'),
]
