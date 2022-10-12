from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import TeacherAccount, StudentAccount
from manager.models import Class, School

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class TeacherRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = TeacherAccount
        fields = ['username', 'password']

class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    student_class = forms.ModelChoiceField(queryset=Class.objects.all())

    class Meta:
        model = StudentAccount
        fields = ['username', 'password', 'student_class']
