from django.urls import path
from . import views

app_name = 'solapi'
urlpatterns = [
    path('', views.info, name='info'),
    path('getPlayer/<str:playerName>', views.getSystem, name='getPlayer'),
    path('getFaction/<str:FactionName>', views.getStar, name='getFaction'),
]
