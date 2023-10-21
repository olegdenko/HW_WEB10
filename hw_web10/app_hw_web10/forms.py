from django.forms import ModelForm, ImageField, CharField, FileInput, TextInput

from .models import Picture


class PictureForm(ModelForm):
    description = CharField(max_length=150)
    path = ImageField()

    class Meta:
        model = Picture
        fields = ["description", "path"]
