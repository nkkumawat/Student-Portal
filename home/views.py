from django.shortcuts import render
from django.http import HttpResponseRedirect
from login.models import Student
# Create your views here.

def home(request):
    if not request.session['stu_roll']:
        return HttpResponseRedirect('/login')
    else:
        stu = Student.objects.filter(stu_roll = request.session['stu_roll'] )
        student = {
            "student" : stu
        }
        return render(request , 'home.html' , student)