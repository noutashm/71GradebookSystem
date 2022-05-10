from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from gradebook.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),

    path('list_semesters', ListSemestersView.as_view(), name='list_semesters'),
    path('create_semester', CreateSemesterView.as_view(), name='create_semester'),
    path('update_semester/<int:pk>', UpdateSemesterView.as_view(), name='update_semester'),
    path('delete_semester/<int:pk>', DeleteSemesterView.as_view(), name='delete_semester'),

    path('list_courses', ListCoursesView.as_view(), name='list_courses'),
    path('create_course', CreateCourseView.as_view(), name='create_course'),
    path('update_course/<int:pk>', UpdateCourseView.as_view(), name='update_course'),
    path('delete_course/<int:pk>', DeleteCourseView.as_view(), name='delete_course'),

    path('list_lecturers', ListLecturersView.as_view(), name='list_lecturers'),
    path('create_lecturer', CreateLecturerView.as_view(), name='create_lecturer'),
    path('update_lecturer/<int:pk>', UpdateLecturerView.as_view(), name='update_lecturer'),
    path('delete_lecturer/<int:pk>', DeleteLecturerView.as_view(), name='delete_lecturer'),

    path('list_students', ListStudentsView.as_view(), name='list_students'),
    path('create_student', CreateStudentView.as_view(), name='create_student'),
    path('update_student/<int:pk>', UpdateStudentView.as_view(), name='update_student'),
    path('delete_student/<int:pk>', DeleteStudentView.as_view(), name='delete_student'),

    path('list_classes', ListClassesView.as_view(), name='list_classes'),
    path('create_class', CreateClassView.as_view(), name='create_class'),
    path('update_class/<int:pk>', UpdateClassView.as_view(), name='update_class'),
    path('delete_class/<int:pk>', DeleteClassView.as_view(), name='delete_class'),

    # path('accounts/', include('django.contrib.auth.urls')),
    # path('login', auth_views.LoginView.as_view(), name='login'),
    # path('logout', auth_views.LogoutView.as_view(), name='logout')
]