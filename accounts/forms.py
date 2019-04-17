from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
        
class UpdateUserForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name','last_name', 'email',]