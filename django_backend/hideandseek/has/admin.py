from django.forms import TextInput
from hideandseek.has.models import *
from django.contrib import admin
from django.db import models

class PositionLogAdmin(admin.ModelAdmin):
    list_display = ("x","y","z","acc","placedBy")
    list_filter = ("placedBy",)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name","x","y","z","lastSeen")
    filter_horizontal = ("hiddenFrom",)

class GameAdmin(admin.ModelAdmin):
    list_display = ("name","x","y","z","ownedBy")
    filter_hirizontal = ("players",)

admin.site.register(PositionLog,PositionLogAdmin)
admin.site.register(Player,PlayerAdmin)
admin.site.register(Game,GameAdmin)
