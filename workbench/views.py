from django.shortcuts import render, redirect
from .models import Game, Slip
from .forms import GameEditForm
from django.contrib import messages


def slip_page(request):
    slip = Slip.objects.all()
    game = Game.objects.all()

    if request.method == "POST":
        pass

    return render(request, "workbench/slip.html", {"slip": slip})


def homepage(request):
    game = Game.objects.all()
    return render(request, "workbench/homepage.html", {"game": game})



def game_UpdateView(request, pk):
    game = Game.objects.get(id=pk)
    slip = Slip.objects.all()

    current_user = request.user

    form = GameEditForm()

    if request.method == "POST":

        if Slip.objects.filter(picked_game=game).exists():
            up_slip = Slip.objects.get(picked_game=game)
            form = GameEditForm(request.POST, instance=up_slip)

            if form.is_valid():
                form.save()

                messages.success(request, 'Slip update successful')
                return redirect('play:slip')

            else:
                return redirect('play:homepage')

        else:
            form = GameEditForm(request.POST)

            if form.is_valid():
                prediction = form.cleaned_data['predict']

                new_slip = Slip.objects.create(user=current_user, picked_game=game, predict=prediction)
                new_slip.save()

                messages.success(request, "Upload success!")
                return redirect('play:homepage')
            
            else:
                return redirect('play:homepage')

    else:
        return render(request, "workbench/game_select_update.html", {"game": game, "form": form, "slip": slip})


def slip_removal(request, pk):
    slip = Slip.objects.get(id=pk)
    slip.delete()

    messages.info(request, 'game has been removed')
    return redirect('play:slip')