from django.contrib import admin

from .models import *
# # Register your models here.
admin.site.register(Player)
admin.site.register(Faction)
admin.site.register(PlayerFaction)
admin.site.register(FactionFaction)
