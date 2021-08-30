from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


app_name = 'users'
urlpatterns = [
    path('newuser/', views.newUser, name='newUser'),
    path('userinfo/', views.UserView.as_view(), name='userinfo'),
    path('userfaction/', views.UserFactionView.as_view(), name='userfaction'),
    path('factioninfo/<int:pk>', views.FactionView.as_view(), name='factioninfo'),
    path('factionfaction/<int:pk>', views.FactionFactionView.as_view(), name='factionfaction'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('getPlayer/<str:playerName>', views.getSystem, name='getPlayer'),
    # path('getFaction/<str:FactionName>', views.getStar, name='getFaction'),
]
