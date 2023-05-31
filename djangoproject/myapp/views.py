from django.shortcuts import render,HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login

# Create your views here.
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        print(form)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                return HttpResponse("<h1>User logged in successfully...<h1>")
    else:
        form = AuthenticationForm()
        return render(request,'myapp/login.html',{'form':form})
