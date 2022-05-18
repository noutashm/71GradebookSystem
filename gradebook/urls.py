from django.contrib.auth.decorators import login_required
from django.urls import path
from gradebook.views import HomePageView, ListSemestersView, CreateSemesterView, UpdateSemesterView, DeleteSemesterView, \
    ListCoursesView, CreateCourseView, UpdateCourseView, DeleteCourseView, ListLecturersView, create_lecturer, \
    create_lecturer_form, UpdateLecturerView, DeleteLecturerView, ListStudentsView, create_student, create_student_form, \
    UpdateStudentView, DeleteStudentView, upload_student_file, ListStudentEnrolmentView, EnrolStudentView, \
    RemoveStudentEnrolmentView, ListClassesView, CreateClassView, UpdateClassView, DeleteClassView, \
    AssignLecturerToClassView, GradeBookSemesterView, gradebook_class, gradebook_student_list, gradebook_grade_student, \
    gradebook_grade_student_form

urlpatterns = [
    path('', HomePageView.as_view(), name="home"),

    path('semesters', login_required(ListSemestersView.as_view()), name='list_semesters'),
    path('semesters/create', login_required(CreateSemesterView.as_view()), name='create_semester'),
    path('semesters/update/<int:pk>', login_required(UpdateSemesterView.as_view()), name='update_semester'),
    path('semesters/delete/<int:pk>', login_required(DeleteSemesterView.as_view()), name='delete_semester'),

    path('courses', login_required(ListCoursesView.as_view()), name='list_courses'),
    path('courses/create', login_required(CreateCourseView.as_view()), name='create_course'),
    path('courses/update/<int:pk>', login_required(UpdateCourseView.as_view()), name='update_course'),
    path('courses/delete/<int:pk>', login_required(DeleteCourseView.as_view()), name='delete_course'),

    path('lecturers', login_required(ListLecturersView.as_view()), name='list_lecturers'),
    path('lecturers/create', create_lecturer, name='create_lecturer'),
    path('lecturers/create_form', create_lecturer_form, name='create_lecturer_form'),
    path('lecturers/update/<int:pk>', login_required(UpdateLecturerView.as_view()), name='update_lecturer'),
    path('lecturers/delete/<int:pk>', login_required(DeleteLecturerView.as_view()), name='delete_lecturer'),

    path('students', login_required(ListStudentsView.as_view()), name='list_students'),
    path('students/create', create_student, name='create_student'),
    path('students/create_form', create_student_form, name='create_student_form'),
    path('students/update/<int:pk>', login_required(UpdateStudentView.as_view()), name='update_student'),
    path('students/delete/<int:pk>', login_required(DeleteStudentView.as_view()), name='delete_student'),
    path('students/upload', upload_student_file, name='upload_student'),
    path('students/enrolments', login_required(ListStudentEnrolmentView.as_view()), name='list_student_enrolment'),
    path('students/enrolments/enrol', login_required(EnrolStudentView.as_view()), name='enrol_student'),
    path('students/enrolments/remove/<int:pk>', login_required(RemoveStudentEnrolmentView.as_view()), name='remove_student_enrolment'),

    path('classes', login_required(ListClassesView.as_view()), name='list_classes'),
    path('classes/create', login_required(CreateClassView.as_view()), name='create_class'),
    path('classes/update/<int:pk>', login_required(UpdateClassView.as_view()), name='update_class'),
    path('classes/delete/<int:pk>', login_required(DeleteClassView.as_view()), name='delete_class'),
    path('classes/assign_lecturer/<int:pk>', login_required(AssignLecturerToClassView.as_view()), name='assign_lecturer_to_class'),

    path('gradebook', login_required(GradeBookSemesterView.as_view()), name='semesters_gradebook'),
    path('gradebook/<int:pk>/classes', gradebook_class, name='classes_gradebook'),
    path('gradebook/<int:pk>/students', gradebook_student_list, name='student_list_gradebook'),
    path('gradebook/grade_student', gradebook_grade_student, name='grade_student'),
    path('gradebook/grade_student_form/<int:pk>', gradebook_grade_student_form, name='grade_student_form'),
]