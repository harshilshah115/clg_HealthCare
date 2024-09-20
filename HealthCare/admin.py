from django.contrib import admin
from HealthCare.models import register,doctor,medicines,appointment,ordermedicines
from django.contrib.admin.models import LogEntry
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

class AppointmentAdmin(admin.ModelAdmin):
  list_display=("app_name",)
admin.site.register(appointment,AppointmentAdmin)

class OrdermedicinesAdmin(admin.ModelAdmin):
  list_display=("medicinename",)
admin.site.register(ordermedicines,OrdermedicinesAdmin)

# LogEntry.objects.all().delete()