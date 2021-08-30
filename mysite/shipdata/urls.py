from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'shitdata'
urlpatterns = [
    path('ship/<int:pk>', views.ShipView.as_view(), name='ship'),
    path('reactor/<int:pk>', views.ReactorView.as_view(), name='reactor'),
    path('hyperdrive/<int:pk>', views.HyperDriveView.as_view(), name='hyperdrive'),
    path('thruster/<int:pk>', views.ThrusterView.as_view(), name='thruster'),
    path('powerbank/<int:pk>', views.PowerBankView.as_view(), name='powerbank'),
    path('lifesupport/<int:pk>', views.LifeSupportView.as_view(), name='lifesupport'),
    path('repulsion/<int:pk>', views.RepulsionView.as_view(), name='repulsion'),
    path('fuel/<int:pk>', views.FuelView.as_view(), name='fuel'),
    path('hull/<int:pk>', views.HullView.as_view(), name='hull'),
    path('weapon/<int:pk>', views.WeaponView.as_view(), name='weapon'),
    path('computer/<int:pk>', views.ComputerView.as_view(), name='computer'),
]
