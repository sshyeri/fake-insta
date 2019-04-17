from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from .models import Profile

class UpdateUserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name', 'email',]
        
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname', 'introduction', ]