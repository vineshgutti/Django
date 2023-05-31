from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout, get_user_model
from .models import User, Profile
from webapp.forms import webform
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
import sys
from django.core.mail import send_mail
import uuid
from .helper import MessageHandler
from django.conf import settings
import random
from django.utils.encoding import force_bytes
from django.shortcuts import resolve_url
from django.contrib.auth.tokens import default_token_generator

from django.utils.http import urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode
from django.urls import reverse

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.sites.shortcuts import get_current_site


from django.utils.translation import gettext_lazy as _


# Create your views here.
def HomePage(request):
    return render(request, "home.html")


@csrf_exempt
def register(request):
    print("hi")

    form = webform()
    if request.method == "POST":
        print("hello")
        print(request.POST)

        name = request.POST.get("name")
        phone_number = request.POST.get("phone_number")
        email = request.POST.get("email")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        my_user = authenticate(
            email=email, password=password, phone_number=phone_number
        )
        print(my_user)

        # try:
        #     print("enters")
        #     if password != password2:
        #         raise Exception
        # except Exception:
        #     sys.exit()

        if password != password2:
            password_mismatched = True
            return render(
                request, "register.html", {"password_mismatched": password_mismatched}
            )

        form = webform(request.POST)
        # print(form)
        print(form.is_valid())
        print(form.errors)

        if form.is_valid():
            print("enters")

            html_message = render_to_string(
                "email_template_name.html",
                {
                    "name": name,
                    "phone_number": phone_number,
                    "email": email,
                },
            )
            plain_message = strip_tags(html_message)
            # message = "name"
            send_mail(
                "hi",
                plain_message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )

            form.save()

            return redirect("/")
        if my_user:
            print("email")
            user = User.objects.get(email=my_user)
            user_exists = True
            print("hello", user_exists)
            return render(request, "register.html", {"user_exists": user_exists})

    return render(request, "register.html", {"form": form})


@csrf_exempt
def LoginPage(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pass1 = request.POST.get("password")
        print(email)
        print(pass1)

        my_user = authenticate(email=email, password=pass1)
        if my_user:
            user_not_exists = False
            user = User.objects.get(email=my_user)
            login(request, user)
            print("jjjj")

            return redirect("/HomePage")

        else:
            user_not_exists = True
            print("hello", user_not_exists)
            return render(request, "login.html", {"user_not_exists": user_not_exists})

    return render(request, "login.html")


def logoutPage(request):
    logout(request)
    return redirect("/")


def mobile_signin(request):
    if request.method == "POST":
        print(request.POST)
        phonenumber = request.POST.get("phone_number")
        print(phonenumber)

        my_user = User.objects.filter(phone_number=phonenumber).first()
        print(my_user)
        if my_user:
            print("SUCCESS")
            user = User.objects.get(email=my_user)
            otp = random.randint(1000, 9999)
            try:
                profile = Profile.objects.get(user=my_user)
                profile.otp = otp
                profile.save()
            except Profile.DoesNotExist:
                profile = Profile.objects.create(user=user, otp=f"{otp}")

            messagehandler = MessageHandler(
                request.POST["phone_number"], otp
            ).send_otp_via_message()
            # uid = profile.uid
            # url = reverse("otp", kwargs={"uid": uid})
            url = reverse("otp")

            return redirect(url)

        else:
            user_not_exists = True

            print("hello", user_not_exists)
            return render(
                request, "mobile_signin.html", {"user_not_exists": user_not_exists}
            )

    return render(request, "mobile_signin.html")


def otp(request):
    # print(uid)
    if request.method == "POST":
        print("otp")
        otp1 = request.POST.get("otp")
        print(otp1)
        profile = Profile.objects.filter(otp=otp1).first()
        print(profile)
        if profile.otp == otp1:
            print("verified")
            print("success")
            return redirect("HomePage")

        return HttpResponse("wrong otp")

    return render(request, "otp.html")


def passwordreset(request):
    print("hi")
    if request.method == "POST":
        email = request.POST.get("email")
        user = User.objects.filter(email=email).first()
        if user:
            print("user_exists")

            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)

            reset_url = reverse(
                "passwordresetconfirm", kwargs={"uidb64": uid, "token": token}
            )
            subject = "hi"
            domain = get_current_site(request).domain

            activate_url = "http://" + domain + reset_url

            message = (
                "You're receiving this email because you requested a password reset for your user account at 127.0.0.1:8000\n"
                + "Please click on following link\n"
                + activate_url
            )

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                uid,
            )

            return redirect("passwordresetsent")
        else:
            user_not_exists = True
            return render(
                request, "password_reset.html", {"user_not_exists": user_not_exists}
            )

    return render(request, "password_reset.html")


def passwordresetsent(request):
    return render(request, "password_reset_sent.html")


def passwordresetconfirm(request, uidb64, token):
    print(token, "hello")
    print(uidb64, "uuid")
    uid = urlsafe_base64_decode(uidb64).decode()
    print(uid)
    user = User.objects.get(pk=uid)
    token = default_token_generator.check_token(user, token)
    print(token)
    if token:
        if request.method == "POST":
            print("hello")
            print(request.POST)
            password = request.POST.get("password")
            new_password2 = request.POST.get("new_password2")
            print(password, new_password2)
            if password == new_password2:
                if user:
                    user.set_password(password)
                    user.save()
                    token_valid = True
                    return render(
                        request,
                        "password_reset_done.html",
                        {"token_valid": token_valid},
                    )
    else:
        token_invalid = True
        return render(
            request, "password_reset_form.html", {"token_invalid": token_invalid}
        )

    return render(request, "password_reset_form.html")


def passwordresetcomplete(request):
    return render(request, "password_reset_done.html")
