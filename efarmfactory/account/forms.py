from django import forms
from django.contrib.auth.models import User
from .models import profile
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model=User
        fields=['username','email']
    
class UserProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=profile
        fields=['profile_pic','Phonenumber','education','other_info']