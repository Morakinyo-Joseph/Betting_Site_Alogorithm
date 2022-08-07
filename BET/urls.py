
from atexit import register
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    path("", include("register.urls", namespace="register")),

    path("play", include("workbench.urls", namespace="play"))
]
