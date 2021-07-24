from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *



class NurseLoginForm(ModelForm):
    class Meta:
        model = Nurse
        fields = ('email', 'password')

class PatientLoginForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('email', 'password')

class HospitalLoginForm(ModelForm):
    class Meta:
        model = Hospital
        fields = ('email', 'password')




class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']