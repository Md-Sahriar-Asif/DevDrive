from logging import addLevelName

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

class RegisterForm(UserCreationForm):
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email address"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter username"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm password"}))

    class Meta:
        model = get_user_model()
        fields = ["email", "username", "password1", "password2"]

class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter firstname"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter lastname"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter username"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email address"}))
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={"class": "form-control", "placeholder": "Upload image"}))
    address = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter address"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter phone"}))
    bio = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Enter bio"}))
    role = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter role"}))

    class Meta:
        model = get_user_model()
        fields = ["first_name", "last_name", "username", "email", "address", "bio", "phone", "role", "profile_pic"]