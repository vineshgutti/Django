from django.shortcuts import render, redirect
from .models import Registration
from .forms import RegistrationForm
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

# from django.contrib.auth.models import AbstractUser


# Create your views here.
def home(request):
    message = None
    print(request.session.items())
    if request.session.get("log", None) == True:
        message = "Login successfully....!"
        del request.session["log"]
    return render(request, "signupapp/base.html", {"message": message})


def signup(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(form.is_valid())
            form.save()
            return redirect("signin")
        else:
            form.errors
    else:
        form = RegistrationForm()
    return render(request, "signupapp/signup.html", {"form": form})


def Login(request):
    if request.method == "POST":
        # import pdb;pdb.set_trace()
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        print(user)
        print(type(user))
        if user is not None:
            login(request, user)
            request.session["log"] = True
            return redirect("/")
    else:
        form = AuthenticationForm()
        return render(request, "signupapp/login.html", {"form": form})


def Logout(request):
    logout(request)
    return redirect("/")
