from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from gradebook.models import *


class DatePickerInput(forms.DateInput):
    input_type = 'date'


class SemesterForm(forms.ModelForm):
    class Meta:
        model = Semester
        fields = ('year', 'semester', 'courses')

        widgets = {
            'year': forms.NumberInput(attrs={'class': 'form-control', 'min': '2000', 'max': '2200'}),
            'semester': forms.Select(attrs={'class': 'form-select'}),
            'courses': forms.SelectMultiple(attrs={'class': 'form-select'}),
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
        fields = ('staffID', 'firstName', 'lastName', 'email', 'course', 'dateOfBirth')

        widgets = {
            'staffID': forms.NumberInput(attrs={'class': 'form-control'}),
            'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'dateOfBirth': DatePickerInput(attrs={'class': 'form-control'}),
        }


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('studentID', 'firstName', 'lastName', 'email', 'dateOfBirth')

        widgets = {
            'studentID': forms.NumberInput(attrs={'class': 'form-control'}),
            'firstName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'lastName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'dateOfBirth': DatePickerInput(attrs={'class': 'form-control'}),
        }


class StudentEnrolmentForm(forms.ModelForm):
    class Meta:
        model = StudentEnrolment
        fields = ('student', 'class1', 'grade', 'gradeTime')

        widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'class1': forms.Select(attrs={'class': 'form-select'}),
            'grade': forms.NumberInput(attrs={'class': 'form-control'}),
            'gradeTime': forms.DateTimeInput(attrs={'class': 'form-control'}),
        }


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('number', 'semester', 'course', 'lecturer')

        widgets = {
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'semester': forms.Select(attrs={'class': 'form-select'}),
            'course': forms.Select(attrs={'class': 'form-select'}),
            'lecturer': forms.Select(attrs={'class': 'form-select'}),
        }


class LecturerToClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('lecturer',)

        widgets = {
            'lecturer': forms.Select(attrs={'class': 'form-select'}),
        }