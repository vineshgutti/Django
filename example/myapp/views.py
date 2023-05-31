from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html', {'name':'Vinesh'})

def add(request):
    # result = int(request.GET["num1"+"num2"])s
    x = int(request.POST["num1"])
    print(type(x))
    y = int(request.POST["num2"])
    print(type(y))
    result=x+y
    return render(request, 'result.html', {'result':result})