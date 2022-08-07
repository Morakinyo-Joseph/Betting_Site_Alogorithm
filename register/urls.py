from django.urls import path
from . import views

app_name = 'register'

urlpatterns = [
    path('', views.landing_page, name="landing_page"),
    
    path('signup', views.signup, name="signup"),
    path('login', views.logging_in, name="login"),
    path('logout', views.logging_out, name="logout"),
]