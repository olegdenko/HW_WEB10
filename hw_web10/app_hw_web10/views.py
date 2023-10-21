import os
from pydoc import describe
from django.shortcuts import render, redirect
from django.conf import settings
from .forms import PictureForm
from .models import Picture


# Create your views here.
def main(request):
    return render(request, "app_hw_web10/index.html", context={"title": "Web 10 hw!"})


def upload(request):
    form = PictureForm(instance=Picture())
    if request.method == "POST":
        form = PictureForm(request.POST, request.FILES, instance=Picture())
        if form.is_valid():
            form.save()
            return redirect(to="app_hw_web10:pictures")
    return render(
        request,
        "app_hw_web10/upload.html",
        context={"title": "Web 10 hw!", "form": form}
    )


def pictures(request):
    pictures = Picture.objects.all
    return render(
        request, "app_hw_web10/pictures.html", context={"title": "Web 10 hw!", "pictures": pictures, "media": settings.MEDIA_URL}
    )


def remove(request, pic_id):
    picture = Picture.objects.filter(pk=pic_id)
    try:
        os.unlink(os.path.join(settings.MEDIA_ROOT, str(picture.first().path)))
    except OSError as e:
        print(e)
    picture.delete()
    return redirect(to="app_hw_web10:pictures")


def edit(request, pic_id):
    if request.method == 'POST':
        description = request.POST.get('description')
        Picture.objects.filter(pk=pic_id).update(description=description)
        return redirect(to="app_hw_web10:pictures")
    
    picture = Picture.objects.filter(pk=pic_id).first()
    return render(request, "app_hw_web10/edit.html", context={"title": "Web 10 hw!", "pic": picture, "media": settings.MEDIA_URL})


def login(request):
    return render(request, "app_hw_web10/login.html", context={"title": "Web 10 hw!"})


def register(request):
    return render(
        request, "app_hw_web10/register.html", context={"title": "Web 10 hw!"}
    )