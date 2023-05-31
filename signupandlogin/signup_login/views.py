from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users
import random
import string


# Create your views here.
def register(request):
    if request.method == "POST":
        data = request.POST
        user = Users.objects.create_user(
            first_name=data["first_name"],
            last_name=data["last_name"],
            username=data["username"],
            email=data["email"],
            password=data["password"],
            gender=data["gender"],
            date_of_birth=data["date_of_birth"],
            phone=data["phone"],
            verify_string="".join(
                random.choices(string.ascii_letters + string.digits, k=20)
            ),
        )
        return HttpResponse("User Registered successfully ...")
    return render(request, "registration.html")


# def login_attempt(request):
#     if request.method == 'POST' :
#         login_input = request.POST.get('username').lower()
#         password = request.POST.get('password')

#         """
#         alternative:
#              if ".com" in login_input
#         """
#         if "@" in login_input:
#             user_obj = User.objects.filter(email = login_input)).first()
#             user = authenticate(email = user_obj.email, password = password )
#         else:
#             user_obj = User.objects.filter(username = login_input).first()
#             user = authenticate(email = user_obj.username, , password = password
#        login(request, user);
#        return render(request, 'login.html',context)
