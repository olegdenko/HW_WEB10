from django.contrib import admin
from django.urls import path, include
from . import views
from .apps import AppHwWeb10Config

app_name = AppHwWeb10Config.name
app_name = "App_HwWeb10"

urlpatterns = [path("", views.main, name="root")]
