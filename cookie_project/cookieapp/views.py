from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    if 'email' in request.COOKIES :
        email = request.COOKIES['email']
        print(email)
        return render(request,'home.html',{'email':email})
    else:
        return render(request, 'home.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        print(email)
        print(request.COOKIES)
        # print(type(request.COOKIES))
        # email=request.COOKIES.get('email')
        response= render(request, 'home.html')
        response.set_cookie('email',email)
        return response
        # login_status = request.COOKIES.get('login_status')
    # return render(request,'login.html')