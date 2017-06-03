from django.contrib import admin
from clinic.models import Patient, Consultation, Drug
# Register your models here.



admin.site.register(Patient)
admin.site.register(Consultation)
admin.site.register(Drug)