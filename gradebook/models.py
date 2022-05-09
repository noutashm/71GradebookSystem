from django.core.validators import MaxValueValidator
from django.db import models

# Planning to revise all this later
from django.urls import reverse


class Semester(models.Model):
    year = models.PositiveIntegerField(validators=[MaxValueValidator(9999)], null=False, blank=False)
    semester = models.PositiveIntegerField(validators=[MaxValueValidator(4)], null=False, blank=False)

    def __str__(self):
        return str(self.year) + " " + str(self.semester)

    def get_absolute_url(self):
        return reverse('list_semesters')

class Course(models.Model):
    code = models.CharField(max_length=50, null=False, blank=False, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('list_courses')

class Lecturer(models.Model):
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
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.number

class Student(models.Model):
    firstName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    dateOfBirth = models.DateField(null=False, blank=False)

    def __str__(self):
        return self.firstName

class StudentEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class1 = models.ForeignKey(Class, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    enrollTime = models.DateTimeField(auto_now_add=True)
    gradeTime = models.DateTimeField()

    def __str__(self):
        return self.student.firstName
