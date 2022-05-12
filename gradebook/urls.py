from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from gradebook.views import *

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),

    path('semesters', ListSemestersView.as_view(), name='list_semesters'),
    path('semesters/create', CreateSemesterView.as_view(), name='create_semester'),
    path('semesters/update/<int:pk>', UpdateSemesterView.as_view(), name='update_semester'),
    path('semesters/delete/<int:pk>', DeleteSemesterView.as_view(), name='delete_semester'),

    path('courses', ListCoursesView.as_view(), name='list_courses'),
    path('courses/create', CreateCourseView.as_view(), name='create_course'),
    path('courses/update/<int:pk>', UpdateCourseView.as_view(), name='update_course'),
    path('courses/delete/<int:pk>', DeleteCourseView.as_view(), name='delete_course'),

    path('lecturers', ListLecturersView.as_view(), name='list_lecturers'),
    path('lecturers/create', CreateLecturerView.as_view(), name='create_lecturer'),
    path('lecturers/update/<int:pk>', UpdateLecturerView.as_view(), name='update_lecturer'),
    path('lecturers/delete/<int:pk>', DeleteLecturerView.as_view(), name='delete_lecturer'),

    path('students', ListStudentsView.as_view(), name='list_students'),
    path('students/create', CreateStudentView.as_view(), name='create_student'),
    path('students/update/<int:pk>', UpdateStudentView.as_view(), name='update_student'),
    path('students/delete/<int:pk>', DeleteStudentView.as_view(), name='delete_student'),
    path('students/upload', upload_student_file, name='upload_student'),

    path('classes', ListClassesView.as_view(), name='list_classes'),
    path('classes/create', CreateClassView.as_view(), name='create_class'),
    path('classes/update/<int:pk>', UpdateClassView.as_view(), name='update_class'),
    path('classes/delete/<int:pk>', DeleteClassView.as_view(), name='delete_class'),
    path('classes/assign_lecturer/<int:pk>', AssignLecturerToClassView.as_view(), name='assign_lecturer_to_class'),

    # path('accounts/', include('django.contrib.auth.urls')),
    # path('login', auth_views.LoginView.as_view(), name='login'),
    # path('logout', auth_views.LogoutView.as_view(), name='logout')
]