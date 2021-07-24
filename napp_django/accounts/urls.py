from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'hospital', views.HospitalViewSet)
router.register(r'patient', views.PatientViewSet)
router.register(r'pain', views.PainViewSet)
router.register(r'nurse', views.NurseViewSet)
router.register(r'medication', views.MedicationViewSet)
router.register(r'times', views.TimeViewSet)

urlpatterns = [
    path('', views.home, name = "home"),
    path('nurse/', views.nurse, name = "nurse"),
    path('patient/', views.patient, name = "patient"),
    path('hospital/', views.hospital, name = "hospital"),
    path('nurselogin/', views.nurseLogin, name = "nurselogin"),
    path('patientlogin/', views.patientLogin, name = "patientlogin"),
    path('hospitallogin/', views.hospitalLogin, name = "hospitallogin"),
    path('addpatient/', views.addPatient, name = "addpatient"),
    path('choose/', views.chooseLogin, name = "chooselogin"),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
