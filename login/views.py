from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from login.forms import LoginForm , SignUpForm
from login.models import Student


# Create your views here.

def auth(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            stu_roll = form.cleaned_data['stu_roll']
            stu_password = form.cleaned_data['stu_password']
            stu_info = Student.objects.filter(stu_roll = stu_roll , stu_password = stu_password)
            request.session['stu_roll'] = stu_roll
            if stu_info:
                return HttpResponseRedirect('/home')
            else:
                return HttpResponse("User Not Found")
    else:
        return HttpResponse(request.method)

def login(request):
    if request.session['stu_roll'] :
            return HttpResponseRedirect('/home')
    return render(request , "login.html" , {})


def sign_up(request):

    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        print(form.errors)
        if form.is_valid():
            student = Student()
            student.stu_name = form.cleaned_data['stu_name']
            student.stu_mail = form.cleaned_data['stu_mail']
            student.stu_password = form.cleaned_data['stu_password']
            student.stu_roll = form.cleaned_data['stu_roll']
            student.stu_address = form.cleaned_data['stu_address']
            student.stu_mobile = form.cleaned_data['stu_mobile']
            student.save()
            request.session['stu_roll'] = student.stu_roll
            return HttpResponseRedirect('/home')

def sign_up_page(request):
    if request.session['stu_roll']:
        return HttpResponseRedirect('/home')
    return render(request , 'signup.html' , {})