from django.shortcuts import render, redirect 
from .models import Student
from django.http import HttpResponseRedirect



def index(request):
	stud = Student.objects.all()
	return render(request, "polls/index.html")

def created(request):
	stud = Student.objects.all()
	return render(request, "polls/created.html")


# сохранение данных в бд
def create(request):
    if request.method == "POST":
        std = Student()
        std.name = request.POST.get("name")
        std.surname = request.POST.get("surname")
        std.group = request.POST.get("group")
        std.language = request.POST.get("language")
        std.expirience = request.POST.get("expirience")
        std.work = request.POST.get("work")
        std.info = request.POST.get("info")
        std.wwork = request.POST.get("wwork")
        std.tema1 = request.POST.get("tema1")
        std.tema2 = request.POST.get("tema2")
        std.tema3 = request.POST.get("tema3")
        std.tema4 = request.POST.get("tema4")
        std.save()
    return HttpResponseRedirect("/created")
    

def completed(request):
	stud = Student.objects.all()
	return render(request, "polls/completed.html")


























