"""tripquery URL Configuration

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
from queryapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="homes"),
    path("trip", views.trip, name="trip"),
    path("timespan", views.timespan, name="timespan"),
    path("sum_entire_trip", views.sum_entire_trip, name="sum_entire_trip"),
    path("avg_entire_trip", views.avg_entire_trip, name="avg_entire_trip"),
    path("boat_avg", views.boat_avg, name="boat_avg"),
    path("trip_sensors", views.trip_sensors, name="trip_sensors"),
]
