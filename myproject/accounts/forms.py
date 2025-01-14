# accounts/forms.py
from django import forms
from django.contrib.auth.models import User
from .models import UserInformation,Blog

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return password2

class UserImageForm(forms.ModelForm):
    class Meta:
        model = UserInformation
        fields = ['image']

   
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content']