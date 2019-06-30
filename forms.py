from django import forms
from register.models import User
from django.contrib.auth.models import User
class RegistrationForm(forms.Form):
    username=forms.CharField(max_length=20)
    password=forms.CharField(max_length=20)
