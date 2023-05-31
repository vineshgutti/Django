from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import (
    PasswordResetForm,
    SetPasswordForm,
)

urlpatterns = [
    path("HomePage", views.HomePage, name="HomePage"),
    path("register", views.register, name="register"),
    path("", views.LoginPage, name="LoginPage"),
    path("logoutPage", views.logoutPage, name="logoutPage"),
    path("passwordreset", views.passwordreset, name="passwordreset"),
    path("passwordresetsent", views.passwordresetsent, name="passwordresetsent"),
    path(
        "reset/<uidb64>/<token>",
        views.passwordresetconfirm,
        name="passwordresetconfirm",
    ),
    path(
        "passwordresetcomplete",
        views.passwordresetcomplete,
        name="passwordresetcomplete",
    ),
    path("mobile_signin/", views.mobile_signin, name="mobile_signin"),
    path("otp/", views.otp, name="otp"),
    # path(
    #     "reset_password/",
    #     auth_views.PasswordResetView.as_view(template_name="password_reset.html"),
    #     name="reset_password",
    # ),
    # path(
    #     "reset_password_sent/",
    #     auth_views.PasswordResetDoneView.as_view(
    #         template_name="password_reset_sent.html"
    #     ),
    #     name="password_reset_done",
    # ),
    # path(
    #     "reset/<uidb64>/<token>/",
    #     auth_views.PasswordResetConfirmView.as_view(
    #         template_name="password_reset_form.html"
    #     ),
    #     name="password_reset_confirm",
    # ),
    # path(
    #     "reset_password_complete/",
    #     auth_views.PasswordResetCompleteView.as_view(
    #         template_name="password_reset_done.html"
    #     ),
    #     name="password_reset_complete",
    # ),
    # path("otp/<str:uid>/", views.otp, name="otp"),
]
