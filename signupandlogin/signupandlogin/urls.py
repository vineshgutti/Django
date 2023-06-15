"""signupandlogin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from signup_login.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", register, name="register"),
    path("emailactivate/<uid>/<verify_string>", email_activate, name="emailactivate"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
    path("profile/<int:id>", profile, name="profile"),
    path("emailchange", changeemail, name="emailchange"),
    path(
        "changeemail/<uid>/<token>/<token1>",
        change_email_activate,
        name="changeemaileactivate",
    ),
    path(
        "emailsendresetpassword", emailsend_passwordreset, name="emailsendresetpassword"
    ),
    path("resetpassword/<uid>/<token>", reset_password, name="resetpassword"),
]
