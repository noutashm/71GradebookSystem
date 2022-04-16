from django.shortcuts import render

# Create your views here.
from gradebook.models import *


def index(request):
    context = {
        "title": "my title",
        "content": "my content"
    }
    render(request, "index.html", context)

def listSemesters(request):
    semesters = Semester.objects.all()
    context = {
        "title": "Semesters",
        "semesters": semesters
    }
    return render(request, "semester/list_semesters.html", context)

def createSemester(request):
    inputYear = request.POST.get("year")
    inputSemester = request.POST.get("semester")
    try:
        semester = Semester(year=inputYear, semester=inputSemester)
        semester.save()
        message = "Semester " + inputSemester + " Created!"
    except:
        message = "Semester Creation Failed!"
    context = {
        "title": "Create Semester",
        "message": message
    }
    return render(request, 'semester/create_semester.html', context)

def createSemesterForm(request):
    context = {
        "title": "Create Semester Form"
    }
    return render(request, 'semester/create_semester_form.html', context)

def updateSemester(request):
    inputID = request.POST.get('id')
    inputYear = request.POST.get("year")
    inputSemester = request.POST.get("semester")
    try:
        semester = Semester.objects.get(id=inputID)
        semester.year = inputYear
        semester.semester = inputSemester
        semester.save()
        message = "Semester " + inputSemester + " Updated!"
    except:
        message = "Semester Update Failed!"
    context = {
        "title": "Update Semester",
        "message": message
    }
    return render(request, 'semester/update_semester.html', context)

def updateSemesterForm(request, id):
    semester = Semester.objects.get(id=id)
    context = {
        "title": "Update Semester Form",
        "category": semester
    }
    return render(request, 'semester/update_semester_form.html', context)

def deleteSemester(request, id):
    try:
        semester = Semester.objects.get(id=id)
        semester.delete()
        message = semester.semester + " Deleted Successfully!"
    except:
        message = "Delete Failed!"
    context = {
        "title": "Delete Semester",
        "message": message
    }
    return render(request, 'semester/delete_semester.html', context)