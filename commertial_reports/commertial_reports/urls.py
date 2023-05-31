"""commertial_reports URL Configuration

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
from commertial_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home),
    path("commertial_reports", views.commertial_reports, name="commertial_reports"),
    path("dscrs_reports", views.dscrs_reports, name="dscrs_reports"),
    path("change_payment", views.payment_method, name="change_payment"),
    path(
        "AddStripePaymentMethod",
        views.AddStripePaymentMethod,
        name="AddStripePaymentMethod",
    ),
    # path("success", views.success, name="success"),
]
