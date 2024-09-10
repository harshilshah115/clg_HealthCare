from django.contrib import admin
from HealthCare.models import register,doctor,medicines
# Register your models here.

class RegisterAdmin(admin.ModelAdmin):
  list_display = ("fullname_reg",)
admin.site.register(register,RegisterAdmin)

class DoctorAdmin(admin.ModelAdmin):
  list_display=("doctor_name",)
admin.site.register(doctor,DoctorAdmin)

class MedicinesAdmin(admin.ModelAdmin):
  list_display=("medicines_name",)
admin.site.register(medicines,MedicinesAdmin)