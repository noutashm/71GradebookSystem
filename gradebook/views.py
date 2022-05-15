import pandas as pd
from django.contrib.auth.models import Group
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.shortcuts import render

from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

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
        student_file = request.FILES['studentFile']
        fs = FileSystemStorage()
        filename = fs.save(student_file.name, student_file)
        uploaded_file_url = fs.url(filename)

        import pandas as panda
        excel_data = pd.read_excel(student_file)
        data = pd.DataFrame(excel_data)
        student_ids = data['ID'].tolist()
        first_names = data['Firstname'].tolist()
        last_names = data['Lastname'].tolist()
        emails = data['Email'].tolist()
        dobs = data['DOB'].tolist()
        courses = data['Course'].tolist()
        classes = data['Class'].tolist()

        i = 0
        while i < len(student_ids):
            student_id = student_ids[i]
            first_name = first_names[i]
            last_name = last_names[i]
            email = emails[i]
            dob = dobs[i]
            dob = str(dob).split(" ")[0]
            password = dob.replace('-', '')
            course = courses[i]
            class1 = classes[i]

            user = User.objects.create_user(username=first_name.lower())
            user.set_password(password)
            user.first_name = first_name
            user.last_name = last_name
            user.email = email
            student_group = Group.objects.get(name='student')
            user.groups.add(student_group)
            user.save()
            student = Student(user=user, studentID=student_id, firstName=first_name, lastName=last_name, email=email,
                              dateOfBirth=dob)
            student.save()

            i = i + 1

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


class GradeBookSemesterView(ListView):
    model = Semester
    template_name = 'gradebook/semesters_gradebook.html'


def gradebook_class(request, pk):
    classes = Class.objects.filter(semester_id=pk)
    studentEnrolment = StudentEnrolment.objects.all()
    context = {
        "classes": classes,
        "studentEnrolment": studentEnrolment
    }
    return render(request, 'gradebook/classes_gradebook.html', context)


def gradebook_student_list(request, pk):
    studentEnrolment = StudentEnrolment.objects.filter(class1_id=pk)
    current_class = Class.objects.get(id=pk)
    context = {
        "semester_id": current_class.semester.id,
        "studentEnrolment": studentEnrolment
    }
    return render(request, 'gradebook/student_list_gradebook.html', context)

def gradebook_grade_student(request):
    id = request.POST.get("id")
    grade = request.POST.get("grade")
    try:
        studentEnrolment = StudentEnrolment.objects.get(id=id)
        studentEnrolment.grade = grade
        studentEnrolment.gradeTime = timezone.now()
        studentEnrolment.save()
        send_mail('Class Grade Notification', 'Your grade has been published! \nPlease check in gradebook :).', 'noutam01@myunitec.ac.nz', [studentEnrolment.student.email], fail_silently=False)
        message = "Student " + studentEnrolment.student.firstName + " graded successfully!"
    except:
        message = "Could not grade " + studentEnrolment.student.firstName + "!"

    context = {
        "message": message,
        "studentEnrolment": studentEnrolment
    }
    return render(request, 'gradebook/grade_student.html', context)


def gradebook_grade_student_form(request, pk):
    studentEnrolment = StudentEnrolment.objects.get(id=pk)
    context = {"studentEnrolment": studentEnrolment}
    return render(request, 'gradebook/grade_student_form.html', context)