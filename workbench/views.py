from django.shortcuts import render
from .models import Game, GameResult, Slip
from .forms import SlipCreationForm


def slip_page(request):
    slip = Slip.objects.all()
    return render(request, "workbench/slip.html", {"slip": slip})


def homepage(request):
    game = Game.objects.all()
    return render(request, "workbench/homepage.html", {"game": game})



def game_UpdateDetail(request, pk):
    game = Game.objects.get(id=pk)
    game_slip = game.slip_set.all()
    return render(request, "workbench/game_select_update-detail.html", {"game": game, "slip": game_slip})