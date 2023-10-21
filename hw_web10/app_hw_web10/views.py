from django.shortcuts import render
from .forms import PictureForm
from .models import Picture


# Create your views here.
def main(request):
    return render(request, "app_hw_web10/index.html", context={"title": "Web 10 hw!"})


def upload(request):
    form = PictureForm(instance=Picture())
    return render(
        request,
        "app_hw_web10/upload.html",
        context={"title": "Web 10 hw!", "form": form}
    )


def pictures(request):
    return render(
        request, "app_hw_web10/pictures.html", context={"title": "Web 10 hw!"}
    )


def login(request):
    return render(request, "app_hw_web10/login.html", context={"title": "Web 10 hw!"})


def register(request):
    return render(
        request, "app_hw_web10/register.html", context={"title": "Web 10 hw!"}
    )
