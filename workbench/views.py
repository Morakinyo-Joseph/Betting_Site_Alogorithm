from django.shortcuts import render, redirect
from .models import Game, GameResult, Slip
from .forms import GameEditForm
from django.contrib import messages


def slip_page(request):
    slip = Slip.objects.all()
    return render(request, "workbench/slip.html", {"slip": slip})


def homepage(request):
    game = Game.objects.all()
    return render(request, "workbench/homepage.html", {"game": game})



def game_UpdateDetail(request, pk):
    game = Game.objects.get(id=pk)
    game_slip = Slip.objects.get(picked_game=game)
    form = GameEditForm(instance=game_slip)

    if request.method == "POST":
        form = GameEditForm(request.POST, instance=game_slip)

        if form.is_valid():
            form.save()

            messages.success(request, "Upload success!")
            return redirect('play:homepage')
        
        else:
            return redirect('play:homepage')

    else:
        return render(request, "workbench/game_select_update-detail.html", {"game": game, "form": form})