from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes, smart_str
from .models import Users
from signup_login import utils
from django.contrib import messages
from .forms import *
import random
import string
from django.db.models import Q

# from .backends import EmailOrUsernameBackend as EoP


# Create your views here.
def register(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        print(type(data))
        form = UserRegistrationForm(data)
        print(form.is_valid())
        print(form.errors)
        if form.is_valid():
            user = Users.objects.create_user(
                first_name=data["first_name"],
                last_name=data["last_name"],
                username=data["username"],
                email=data["email"],
                password=data["password"],
                gender=data["gender"],
                date_of_birth=data["dob"],
                phone=data["phone"],
                verify_string="".join(
                    random.choices(string.ascii_letters + string.digits, k=20)
                ),
            )
            print(user)
            # uid = urlsafe_base64_encode(force_bytes(user.id))
            # print(uid)
            # link = (
            #     "http://127.0.0.1:8000/emailactivate/" + uid + "/" + user.verify_string
            # )
            # print(link)
            # body = "Click following link to Reset your password:" + link
            # data = {
            #     "subject": "Verify your account",
            #     "body": body,
            #     "to_email": user.email,
            # }
            # print(data)
            # token = default_token_generator.make_token(user)
            utils.send_email(user)
            messages.success(
                request,
                "User Registered successfully. Please check your email to verify your account.",
            )
            return redirect("login")
        else:
            return render(
                request, "registration.html", {"form": form}
            )  # here we need to pass the 'form' object if you don't pass the form object form.errors will not display.

    return render(request, "registration.html")


def email_activate(request, uid, verify_string):
    id = smart_str(urlsafe_base64_decode(uid))
    user = Users.objects.get(id=id)
    try:
        user
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is None:
        return HttpResponse("User not found")
    if not (user, verify_string):
        return HttpResponse(
            "Token is invalid or expired. Please request another confirmation email by signing in."
        )
    user.status = "Active"
    user.save()
    messages.success(
        request, "Successfully, your EMAIL ID is verified. you can login now."
    )
    return redirect("login")
    # return HttpResponse("user verified successfully")


def login_view(request):
    if request.method == "POST":
        usernameInput = request.POST.get("username_or_email")
        password = request.POST.get("password")
        # print(request.POST)
        try:
            my_user = Users.objects.get(
                Q(username__exact=usernameInput) | Q(email__exact=usernameInput)
            )
        except Users.DoesNotExist:
            my_user = None
        if my_user is not None:
            email = my_user.email
            # print(email)
            if my_user.status == "Active":
                # my_user.check_password(password)
                # print(my_user.check_password(password))
                user = authenticate(request, username=email, password=password)
                print(user)
                if user is not None:
                    # print("authenticated")
                    login(request, user)
                    # return HttpResponse("User login successfully")
                    messages.success(request, "User authenticated successfully.")
                    return redirect("profile/" + str(user.id))
                else:
                    messages.error(request, "email or password is not valid")
                    return redirect("login")
            else:
                messages.error(
                    request,
                    "your email is not verified, Please check your register EMAIL ID.",
                )
                return redirect("login")
        else:
            messages.error(request, "Username or password is Invalid")
            return redirect("login")
    return render(request, "login.html")


def profile(request, id):
    user = Users.objects.get(id=id)
    return render(request, "profile.html", {"user": user})


def changeemail(request):
    if request.method == "POST":
        form = ChangeEmailForm(request.POST)
        print(request.user.email)
        id = request.user.id
        print(id)
        # print(form.is_valid())
        if form.is_valid():
            email = form.cleaned_data.get("email")
            print(email)
            user = Users.objects.get(id=id)
            token = PasswordResetTokenGenerator().make_token(user)
            utils.send_changeemail(user, email, token)
            messages.success(
                request,
                "A verification link is sent your new email, please verify emailID",
            )
            # user.email = email
            # user.status = "Inactive"
            # user.save()
            return redirect("logout")
        else:
            return render(request, "change_email.html", {"form": form})
    else:
        return render(request, "change_email.html")


def change_email_activate(request, uid, token, token1):
    id = smart_str(urlsafe_base64_decode(uid))
    user = Users.objects.get(id=id)
    check_token = PasswordResetTokenGenerator().check_token(user, token)
    email = utils.string_b64decode(token1)
    print(email)

    if not check_token:
        messages.error(request, "Token is not valid or expired please enter your email")
        return redirect("emailchange")
    else:
        try:
            user
        except (TypeError, ValueError, OverflowError, user.DoesNotExist):
            user = None
        if user is None:
            return HttpResponse("User not found")
        user.email = email
        user.save()
        messages.success(
            request, "Successfully, your NEW EMAIL ID is verified. you can login now."
        )
        return redirect("login")


def emailsend_passwordreset(request):
    if request.method == "POST":
        form = EmailSendResetPasswordForm(request.POST)
        print(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            print(email)
            user = Users.objects.get(email=email)
            print(user)
            # uid = urlsafe_base64_encode(force_bytes(user.id))
            # print(type(uid))
            token = PasswordResetTokenGenerator().make_token(user)
            # print(token)
            utils.send_resetpasswordemail(user, token)
            messages.success(
                request, "Reset password link send to email please check your Email"
            )
            return redirect("emailsendresetpassword")
        else:
            return render(request, "reset_password.html", {"form": form})
    else:
        return render(request, "reset_password.html")


def reset_password(request, uid, token):
    id = smart_str(urlsafe_base64_decode(uid))
    user = Users.objects.get(id=id)
    check_token = PasswordResetTokenGenerator().check_token(user, token)
    if not check_token:
        messages.error(request, "Token is not valid or expired please enter your email")
        return redirect("emailsendresetpassword")
    else:
        if request.method == "POST":
            form = ChangePasswordForm(request.POST)
            if form.is_valid():
                password = form.cleaned_data.get("confirm_password")
                user.set_password(password)
                user.save()
                messages.success(request, "Password Reset successfully")
                return redirect("logout")
            else:
                return render(request, "change_password.html", {"form": form})
        else:
            return render(request, "change_password.html")


def logout_view(request):
    logout(request)
    # messages.success(request, "logout successfully")
    return redirect("login")


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
