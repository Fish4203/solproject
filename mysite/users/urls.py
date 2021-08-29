from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'solapi'
urlpatterns = [
    path('', views.HelloView.as_view(), name='hello'),
    path('newuser', views.newUser, name='newUser'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('getPlayer/<str:playerName>', views.getSystem, name='getPlayer'),
    # path('getFaction/<str:FactionName>', views.getStar, name='getFaction'),
]
