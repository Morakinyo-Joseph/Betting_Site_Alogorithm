from django.urls import path
from . import views

app_name = "workbench"

urlpatterns = [
    path('homepage', views.homepage, name="homepage"),

    path('slip', views.slip_page, name="slip"),

    path('game-UpdateDetail/<str:pk>', views.game_UpdateView, name="game-update-detail"),
]
