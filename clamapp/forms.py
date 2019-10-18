from django import forms
from .models import Image

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['post','likes','profile','comments','user']
        widgets = {
            'likes': forms.CheckboxSelectMultiple(),
        }