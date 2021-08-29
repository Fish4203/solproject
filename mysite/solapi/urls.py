from django.urls import path
from . import views

app_name = 'solapi'
urlpatterns = [
    path('', views.info, name='info'),
    path('system/<int:pk>',  views.SystemView.as_view(), name='system'),
    path('planet/<int:pk>',  views.PlanetView.as_view(), name='planet'),
    path('asteroid/<int:pk>',  views.AsteroidView.as_view(), name='asteroid'),
    path('star/<int:pk>',  views.StarView.as_view(), name='star'),
]
