from django import forms
from django.contrib.auth.models import User
from django.forms import widgets

from webapp.models import Image

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['photo', 'sign']

