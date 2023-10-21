from django.contrib import admin
from django.urls import path, include
from . import views

# app_name = AppHwWeb10Config.name
app_name = "app_hw_web10"

urlpatterns = [
    path("", views.main, name="root"),
    path("upload/", views.upload, name="upload"),
    path("pictures/", views.pictures, name="pictures"),
    path("pictures/edit/<int:pic_id>", views.edit, name="edit"),
    path("pictures/remove/<int:pic_id>", views.remove, name="remove"),
    path("login/", views.login, name="SignIn"),
    # path("register/", views.register, name="SignUp"),
]
