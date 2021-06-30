from rest_framework import serializers

from .models import *

class HospitalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class PainSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pain
        fields = '__all__'

class NurseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'

class MedicationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class TimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = times
        fields = '__all__'