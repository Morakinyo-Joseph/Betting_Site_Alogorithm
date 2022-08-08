from math import gamma
from django.contrib import admin
from .models import Game, GameResult, Slip, Ticket

# Register your models here.

admin.site.register(Game)
admin.site.register(GameResult)
admin.site.register(Slip)
admin.site.register(Ticket)

