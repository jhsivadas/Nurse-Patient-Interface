from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
# Create your views here.
from .forms import *
from .models import *
from rest_framework import viewsets
from .serializer import *
from django.contrib import messages

def addPatient(request):
    email = request.session['email']
    context = {'email': email}
    return render(request, 'accounts/addpatient.html', context)

# Make 3 login pages for nurse patients and hospitals
def nurseLogin(request):
    form = NurseLoginForm()
    if form.is_valid():
        form.save()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        obj = Nurse.objects.filter(email=email).exists()
        pass_check = Nurse.objects.filter(password=password).exists()

        if obj and pass_check:
            request.session['email'] = email
            return redirect('/nurse/')
        else:
            return render(request, 'accounts/nurselogin.html', {'form':form, 'failed':True})
    else:
        return render(request, 'accounts/nurselogin.html', {'form':form, 'failed':False})

def patientLogin(request):
    form = PatientLoginForm()
    if form.is_valid():
        form.save()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        obj = Patient.objects.filter(email=email).exists()
        pass_check = Patient.objects.filter(password=password).exists()

        if obj and pass_check:
            request.session['email'] = email
            return redirect('/patient/')
        else:
            return render(request, 'accounts/patientlogin.html', {'form':form, 'failed':True})
    return render(request, 'accounts/patientlogin.html', {'form':form, 'failed':False})

def hospitalLogin(request):
    form = HospitalLoginForm()
    if form.is_valid():
        form.save()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        obj = Hospital.objects.filter(email=email).exists()
        pass_check = Hospital.objects.filter(password=password).exists()

        if obj and pass_check:
            request.session['email'] = email
            return redirect('/hospital/')
        else:
            return render(request, 'accounts/hospitallogin.html', {'form': form, 'failed': True})
    return render(request, 'accounts/hospitallogin.html', {'form': form, 'failed': False})

def chooseLogin(request):
    return render(request, 'accounts/chooselogin.html')


# Check if form submission is valid
    # form = CreateUserForm()

    # if request.method == 'Get':
    #     form = CreateUserForm(request.Get)
    #     if form.is_valid():
    #         form.save()
    # context = {'form':form}

def home(request):
    return render(request, 'accounts/home.html')

def nurse(request):
    patient = Patient.objects.all()
    pain = Pain.objects.all()
    email = request.session['email']
    context = {'patient' : patient, 'email':email}
    return render(request, 'accounts/nurse.html', context)

def patient(request):
    email = request.session['email']
    context = {'email':email}
    return render(request, 'accounts/patient.html', context)

def hospital(request):
    email = request.session['email']
    context = {'email':email}
    return render(request, 'accounts/hospital.html', context)

def apiview(request):
    return HttpResponse("API VIEW")

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
