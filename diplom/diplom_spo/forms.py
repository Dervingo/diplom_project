from django import forms

from .models import Diplom


class DiplomForm(forms.ModelForm):
    class Meta:
        model = Diplom
        fields = ('org_name', 'qualification', 'ser_number', 'reg_number',
                  'grant_date', 'student_name', 'speciality', 'chairman',
                  'supervisor', 'year', 'copy', )
