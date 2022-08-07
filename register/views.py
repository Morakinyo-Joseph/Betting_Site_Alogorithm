from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import User


def landing_page(request):
    return render(request, 'landing_page.html')


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if len(email) > 0:

            if len(username) > 0:

                if len(password1) > 0:

                    if password1 == password2:
                        if User.objects.filter(email=email).exists():
                            messages.info(request, 'Email address already exists')
                            return redirect('register:signup')

                        elif User.objects.filter(username=username).exists():
                            messages.info(request, 'username already exists')
                            return redirect('register:signup')

                        else:
                            new_user = User.objects.create_user(username=username, password=password1, email=email,
                                                                        first_name=first_name, last_name=last_name)
                            new_user.save()
                            return redirect('register:login')
                    else:
                            messages.info(request, 'Passwords do not match')
                            return redirect('register:signup')
                else:
                    messages.info(request, 'Password field required')
                    return redirect('register:signup')
            else:
                messages.info(request, 'username field required')
                return redirect('register:signup')
            
        else:
            messages.info(request, 'Email field required')
            return redirect('register:signup')

    else:
        return render(request, "register/signup.html")


def logging_in(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('play:homepage')
        else:
            messages.info(request, 'Invalid username/password')
            return redirect('register:login')

    else:
        return render(request, "register/login.html")


def logging_out(request):
    logout(request)
    return redirect('register:login')