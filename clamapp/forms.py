from django import forms
from .models import Image,Profile

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['post','likes','profile','comments','user']
        widgets = {
            'likes': forms.CheckboxSelectMultiple(),
        }
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user_id']