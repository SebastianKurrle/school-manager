from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import TeacherAccount

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class TeacherRegistrationForm(UserCreationForm):
    class Meta:
        model = TeacherAccount
        fields = ['username', 'password1', 'password2']
