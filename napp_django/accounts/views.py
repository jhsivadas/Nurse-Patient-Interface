from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
# Create your views here.
from .models import *
from rest_framework import viewsets
from .serializer import *

def registerPage(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        user.save()
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/register.html')


class HospitalViewSet(viewsets.ModelViewSet):
    queryset = Hospital.objects.all().order_by('name')
    serializer_class = HospitalSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('id')
    serializer_class = PatientSerializer

class PainViewSet(viewsets.ModelViewSet):
    queryset = Pain.objects.all().order_by('date_created')
    serializer_class = PainSerializer

class NurseViewSet(viewsets.ModelViewSet):
    queryset = Nurse.objects.all().order_by('id')
    serializer_class = NurseSerializer

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all().order_by('name')
    serializer_class = MedicationSerializer

class TimeViewSet(viewsets.ModelViewSet):
    queryset = times.objects.all().order_by('name')
    serializer_class = TimeSerializer


    # form = CreateUserForm()

    # Takes in form data/user registration
    # if request.method == 'POST':
    #     options = request.POST['options']
    #     first_name = request.POST['first_name']
    #     last_name = request.POST['last_name']
    #     username = request.POST['username']
    #     email = request.POST['email']
    #     password1 = request.POST['password1']
    #     password2 = request.POST['password2']
    #     if (password1 != password2):
    #         print("Passwords do not match")
    #     elif (User.objects.filter(username=username).exists()):
    #         print("Username is taken")
    #     elif (User.objects.filter(email=email).exists()):
    #         print("Email is taken")
    #     else:
    #         user = User.objects.create_user(options=options, first_name = first_name,
    #         last_name = last_name, username = username, email = email,
    #         password1 = password1, password2 = password2)
    #
    #
    #     user.save()
    #     return redirect('/')
        # form = CreateUserForm(request.POST)
        # if form.is_valid:
        #     form.save()


def home(request):
    return render(request, 'accounts/home.html')

def nurse(request):
    patient = Patient.objects.all()
    pain = Pain.objects.all()
    context = {'patient' : patient}
    return render(request, 'accounts/nurse.html', context)

def apiview(request):
    return HttpResponse("API VIEW")