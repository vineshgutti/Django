from django.urls import path
from rest_app.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", register, name="register"),
    path("login", login, name="login"),
    path("profile", profile, name="profile"),
    path("changepassword", change_password, name="changepassword"),
    path(
        "send_email_password_reset",
        email_send_reset_password,
        name="send_email_password_reset",
    ),
    path("reset_password/<uid>/<token>", user_password_reset, name="reset_password")
    # path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
