from django.shortcuts import render,redirect
from .models import Registration
from .forms import RegistrationForm
from django.http import HttpResponse
# from django.contrib.auth.models import AbstractUser

# Create your views here.
def home(request):
    return render(request, 'signupapp/base.html')
def signup(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            print(form.is_valid())
            form.save()
            return HttpResponse('Registered successfully')
        else:
            form.errors
    else:
        form=RegistrationForm()
    return render(request,'signupapp/signup.html',{'form':form})