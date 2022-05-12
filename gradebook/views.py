from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from gradebook.forms import *
from gradebook.models import *


class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Home'
        context["semesters"] = Semester.objects.all()
        return context


class ListSemestersView(ListView):
    model = Semester
    template_name = 'semester/list_semesters.html'


class CreateSemesterView(CreateView):
    model = Semester
    form_class = SemesterForm
    template_name = 'semester/create_semester.html'


class UpdateSemesterView(UpdateView):
    model = Semester
    form_class = SemesterForm
    template_name = 'semester/update_semester.html'


class DeleteSemesterView(DeleteView):
    model = Semester
    template_name = 'semester/delete_semester.html'
    success_url = reverse_lazy('list_semesters')


class ListCoursesView(ListView):
    model = Course
    template_name = 'course/list_courses.html'


class CreateCourseView(CreateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/create_course.html'


class UpdateCourseView(UpdateView):
    model = Course
    form_class = CourseForm
    template_name = 'course/update_course.html'


class DeleteCourseView(DeleteView):
    model = Course
    template_name = 'course/delete_course.html'
    success_url = reverse_lazy('list_courses')


class ListLecturersView(ListView):
    model = Lecturer
    template_name = 'lecturer/list_lecturers.html'


class CreateLecturerView(CreateView):
    model = Lecturer
    form_class = LecturerForm
    template_name = 'lecturer/create_lecturer.html'


class UpdateLecturerView(UpdateView):
    model = Lecturer
    form_class = LecturerForm
    template_name = 'lecturer/update_lecturer.html'


class DeleteLecturerView(DeleteView):
    model = Lecturer
    template_name = 'lecturer/delete_lecturer.html'
    success_url = reverse_lazy('list_lecturers')


class ListStudentsView(ListView):
    model = Student
    template_name = 'student/list_students.html'


class CreateStudentView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/create_student.html'


class UpdateStudentView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/update_student.html'


class DeleteStudentView(DeleteView):
    model = Student
    template_name = 'student/delete_student.html'
    success_url = reverse_lazy('list_students')


def upload_student_file(request):
    if request.method == 'POST' and request.FILES['studentFile']:
        studentFile = request.FILES['studentFile']
        fs = FileSystemStorage()
        filename = fs.save(studentFile.name, studentFile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'student/upload_student.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'student/upload_student.html')


class ListClassesView(ListView):
    model = Class
    template_name = 'class/list_classes.html'


class CreateClassView(CreateView):
    model = Class
    form_class = ClassForm
    template_name = 'class/create_class.html'


class UpdateClassView(UpdateView):
    model = Class
    form_class = ClassForm
    template_name = 'class/update_class.html'


class AssignLecturerToClassView(UpdateView):
    model = Class
    form_class = LecturerToClassForm
    template_name = 'class/assign_lecturer_to_class.html'


class DeleteClassView(DeleteView):
    model = Class
    template_name = 'class/delete_class.html'
    success_url = reverse_lazy('list_classes')


class ListStudentEnrolmentView(ListView):
    model = StudentEnrolment
    template_name = 'student/enrolment/list_student_enrolment.html'


class EnrolStudentView(CreateView):
    model = StudentEnrolment
    form_class = StudentEnrolmentForm
    template_name = 'student/enrolment/enrol_student.html'


class RemoveStudentEnrolmentView(DeleteView):
    model = StudentEnrolment
    template_name = 'student/enrolment/remove_student_enrolment.html'
    success_url = reverse_lazy('list_student_enrolment')
