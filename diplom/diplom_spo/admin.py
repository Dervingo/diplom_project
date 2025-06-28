from django.contrib import admin
from .models import Diplom


@admin.register(Diplom)
class DiplomAdmin(admin.ModelAdmin):
    list_display = ('pk', 'org_name', 'qualification', 'ser_number', 'reg_number', 
                  'grant_date', 'student_name', 'speciality', 'chairman',
                  'supervisor', 'year', 'copy', )
    search_fields = ('student_name', 'org_name', 'year',)
