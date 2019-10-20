from django import forms
from .models import Image,Profile, Comments

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
        
class commentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['commented_by','commented_image']
        widgets = {
            'likes': forms.CheckboxSelectMultiple(),
        }        