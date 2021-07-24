from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Nurse)
admin.site.register(Patient)
admin.site.register(Hospital)
admin.site.register(Pain)
admin.site.register(Medication)
admin.site.register(times)

