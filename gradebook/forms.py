from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from gradebook.models import *


class DatePickerInput(forms.DateInput):
    input_type = 'date'

class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ('year', 'semester')

        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'semester': forms.NumberInput(attrs={'class': 'form-control'})
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('code', 'name')

        widgets = {
            'code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Code'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'})
        }

class LecturerForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ('firstName', 'lastName', 'email', 'course', 'dateOfBirth')

        widgets = {
            'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'dateOfBirth': DatePickerInput(attrs={'class': 'form-control'}),
        }