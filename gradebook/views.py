from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import *

from gradebook.forms import *
from gradebook.models import *


# def index(request):
#     context = {
#         "title": "my title",
#         "content": "my content"
#     }
#     render(request, "index.html", context)

class HomePageView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = 'Home'
        context["semesters"] = Semester.objects.all()
        return context

class ListSemesters(ListView):
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

class ListCourses(ListView):
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

class ListLecturers(ListView):
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