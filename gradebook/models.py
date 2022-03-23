from django.core.validators import MaxValueValidator
from django.db import models

# Planning to revise all this later
class Semester(models.Model):
    year = models.PositiveIntegerField(validators=[MaxValueValidator(9999)], null=False, blank=False)
    semester = models.PositiveIntegerField(validators=[MaxValueValidator(4)], null=False, blank=False)

class Course(models.Model):
    code = models.CharField(max_length=50, null=False, blank=False, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False)

class Lecturer(models.Model):
    firstName = models.CharField(max_length=100, null=False, blank=False)
    lastName = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    dateOfBirth = models.DateField(null=False, blank=False)

class Class(models.Model):
    number = models.PositiveIntegerField(null=False, blank=False)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)

class Student(models.Model):
    firstName = models.CharField(max_length=50, null=False, blank=False)
    lastName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    dateOfBirth = models.DateField(null=False, blank=False)

class StudentEnrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class1 = models.ForeignKey(Class, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField(validators=[MaxValueValidator(100)])
    enrollTime = models.DateTimeField(auto_now_add=True)
    gradeTime = models.DateTimeField()
