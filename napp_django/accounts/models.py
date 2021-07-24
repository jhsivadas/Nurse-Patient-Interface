from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms

# Create your models here.


class Hospital(models.Model):
	id = models.AutoField(primary_key=True)
	email = models.CharField(max_length=200, null=True)
	password = models.CharField(max_length=200, null=True)
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Patient(models.Model):
	STATUS = (
			('Under Care', 'Under Care'),
			('Discharged', 'Discharged'),
			) 
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	password = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True, blank=True)
	email = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	hospital = models.ForeignKey(Hospital, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name

class Pain(models.Model):
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	level = models.IntegerField(null=True)
	patient = models.ForeignKey(Patient, null=True, on_delete= models.SET_NULL)
	
	def __str__(self):
		return self.patient.name

class Nurse(models.Model):
	STATUS = ( 
			('On Duty', 'On Duty'),
			('Off Duty', 'Off Duty'),
			) 
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=200, null=True)
	password = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	patients = models.ManyToManyField(Patient)
	hospital = models.ForeignKey(Hospital, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.name

class Medication(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class times(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	patients = models.ForeignKey(Patient, null=True, on_delete=models.SET_NULL)
	dosage = models.CharField(max_length=200, null=True)
	medications = models.ForeignKey(Medication, null=True, on_delete=models.SET_NULL)
	start = models.DateTimeField(null=True, blank=True)
	end = models.DateTimeField(null=True, blank=True)
	time1 = models.TimeField(null=True, blank=True)
	time2 = models.TimeField(null=True, blank=True)
	time3 = models.TimeField(null=True, blank=True)
	time4 = models.TimeField(null=True, blank=True)
	time5 = models.TimeField(null=True, blank=True)
	time6 = models.TimeField(null=True, blank=True)
	time7 = models.TimeField(null=True, blank=True)
	time8 = models.TimeField(null=True, blank=True)

	def __str__(self):
		return self.name
	

