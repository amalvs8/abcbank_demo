from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import secrets

from bankapp.models import District


# Create your views here.


def register(request):
    districts = District.objects.all()
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST['last_name']
        username = request.POST["username"]
        password = request.POST["password"]
        c_password = request.POST["c_password"]
        if password == c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exist")
                return redirect("credentials:register")
            else:
                user = User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password
                )
                user.save()
                return redirect("credentials:login")
        else:
            messages.info(request, "Password didn't match")
            return redirect("credentials:register")
    return render(request, 'register.html', {'district': districts})


def login(request):
    districts = District.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(
            username=username,
            password=password
        )
        if user is not None:
            auth.login(request, user)
            return redirect("bankapp:home")
        else:
            messages.info(request, "Username or Password entered is incorrect")
            return redirect("credentials:login")
    return render(request, 'login.html', {'district': districts})


def logout(request):
    auth.logout(request)
    return redirect('/')


def redirection(request):
    return redirect('/')
