from django.contrib import admin
from django.urls import path, include

from gradebook.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),

    path('list_semesters', ListSemesters.as_view(), name='list_semesters'),
    path('create_semester', CreateSemesterView.as_view(), name='create_semester'),
    path('update_semester/<int:pk>', UpdateSemesterView.as_view(), name='update_semester'),
    path('delete_semester/<int:pk>', DeleteSemesterView.as_view(), name='delete_semester'),

    path('list_courses', ListCourses.as_view(), name='list_courses'),
    path('create_course', CreateCourseView.as_view(), name='create_course'),
    path('update_course/<int:pk>', UpdateCourseView.as_view(), name='update_course'),
    path('delete_course/<int:pk>', DeleteCourseView.as_view(), name='delete_course'),

    path('list_lecturers', ListLecturers.as_view(), name='list_lecturers'),
    path('create_lecturer', CreateLecturerView.as_view(), name='create_lecturer'),
    path('update_lecturer/<int:pk>', UpdateLecturerView.as_view(), name='update_lecturer'),
    path('delete_lecturer/<int:pk>', DeleteLecturerView.as_view(), name='delete_lecturer'),
]