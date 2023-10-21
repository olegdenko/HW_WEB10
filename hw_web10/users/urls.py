import imp
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .forms import LoginForm
from .views import RegisterView

# app_name = AppHwWeb10Config.name
app_name = "users"

urlpatterns = [
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signin/", LoginView.as_view(template_name='users/signin.html', authentication_form=LoginForm, redirect_authenticated_user=True), name="login"),
    path("signup/", RegisterView.as_view(), name="register"),
]
