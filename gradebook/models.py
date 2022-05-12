from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from django.db import models

# Planning to revise all this later
from django.urls import reverse

class Course(models.Model):
    code = models.CharField(max_length=50, null=False, blank=False, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list_courses')

class Semester(models.Model):
    SEMESTERS = [
        ('S1', 'S1'),
        ('S2', 'S2'),
        ('S3', 'S3'),
        ('S4', 'S4')
    ]

    year = models.PositiveIntegerField(validators=[MaxValueValidator(2200)], null=False, blank=False)
    semester = models.CharField(choices=SEMESTERS, max_length=2, default='S1')
    courses = models.ManyToManyField(Course, blank=True, null=True)

    def __str__(self):
        return str(self.year) + " " + str(self.semester)

    def get_absolute_url(self):
        return reverse('list_semesters')

class Lecturer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    staffID = models.PositiveIntegerField(null=False, blank=False, unique=True)
    firstName = models.CharField(max_length=100, null=False, blank=False)
    lastName = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    dateOfBirth = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.firstName + " " + self.lastName

    def get_absolute_url(self):
        return reverse('list_lecturers')

class Class(models.Model):
    number = models.PositiveIntegerField(null=False, blank=False)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return str(self.number)

    def get_absolute_url(self):
        return reverse('list_classes')

class Student(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    studentID = models.PositiveIntegerField(null=False, blank=False, unique=True)
    firstName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    dateOfBirth = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.firstName + " " + self.lastName

    def get_absolute_url(self):
        return reverse('list_students')

class StudentEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class1 = models.ForeignKey(Class, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    enrollTime = models.DateTimeField(auto_now_add=True)
    gradeTime = models.DateTimeField()

    def __str__(self):
        return self.student.firstName + " " + str(self.class1.number)
