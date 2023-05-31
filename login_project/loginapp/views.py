from django.shortcuts import render, redirect
from loginapp.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login


# Create your views here.
def Signup(request):
    if request.method == "POST":
        # import pdb;pdb.set_trace()
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            form = SignupForm()
            return render(request, "loginapp/signup.html", {"form": form})

    else:
        form = SignupForm()
        return render(request, "loginapp/signup.html", {"form": form})


def Login(request):
    if request.method == "POST":
        # import pdb;pdb.set_trace()
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("success")
    else:
        form = AuthenticationForm()
        return render(request, "loginapp/login.html", {"form": form})


def Success(request):
    return render(request, "loginapp/success.html")
