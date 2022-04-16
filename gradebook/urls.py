from django.contrib import admin
from django.urls import path, include

from gradebook.views import *

urlpatterns = [
    path('', listSemesters, name="home"),
    path('list_semesters', listSemesters, name="list_semesters"),
    path('create_semester', createSemester, name='create_semester'),
    path('create_semester_form', createSemesterForm, name='create_semester_form'),
    path('update_semester', updateSemester, name='update_semester'),
    path('update_semester_form/<int:id>', updateSemesterForm, name='update_semester_form'),
    path('delete_semester/<int:id>', deleteSemester, name='delete_semester'),
]