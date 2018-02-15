from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from user.forms import LoginForm , SignUpForm , ChangePasswordFrom
from user.models import Student , Branch , Semester , Course
from django.contrib.auth.hashers import make_password , check_password

# Create your views here.

def auth(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            stu_roll = form.cleaned_data['stu_roll']
            stu_password = form.cleaned_data['stu_password']
            stu_info = Student.objects.get(stu_roll = stu_roll)
            # print(check_password(stu_password ,stu_info.stu_password ))
            if check_password(stu_password ,stu_info.stu_password ):
                request.session['stu_roll'] = stu_roll
                return HttpResponseRedirect('/home')
            else:
                return HttpResponse("User Not Found")
    else:
        return HttpResponse(request.method)

def login(request):
    if 'stu_roll' in request.session :
            return HttpResponseRedirect('/home')
    return render(request , "login.html" , {})

def sign_up(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        print(form.errors)
        if form.is_valid():
            student = Student()
            student.stu_name = form.cleaned_data['stu_name']
            student.stu_mail = form.cleaned_data['stu_mail']
            student.stu_password =make_password(form.cleaned_data['stu_password'])
            student.stu_roll = form.cleaned_data['stu_roll']
            student.stu_address = form.cleaned_data['stu_address']
            student.stu_mobile = form.cleaned_data['stu_mobile']
            student.stu_branch_id = form.cleaned_data['stu_branch_id']
            student.stu_course_id = form.cleaned_data['stu_course_id']
            student.stu_semester_id = form.cleaned_data['stu_semester_id']
            student.save()
            # print(student.id)
            request.session['stu_roll'] = student.stu_roll
            return HttpResponseRedirect('/home')

def sign_up_page(request):
    if 'stu_roll' in request.session:
        return HttpResponseRedirect('/home')
    else:
        branch = Branch.objects.all()
        semester =Semester.objects.all()
        course =Course.objects.all()
        student = {
            "branch": branch,
            "semester": semester,
            "course" : course
        }
        return render(request , 'signup.html' , student)

def logout(request):
    if 'stu_roll' in request.session:
        del request.session['stu_roll']
        return HttpResponseRedirect('/user/login')
    else:
        return HttpResponseRedirect('/user/login')

def change_password(request):
    if request.method == "POST":
        form = ChangePasswordFrom(request.POST)
        print(form.errors)
        if form.is_valid():
            student = Student.objects.get(stu_roll = request.session['stu_roll'])
            if check_password( form.cleaned_data['old_password'] , student.stu_password):
                student.stu_password = make_password(form.cleaned_data['new_password'])
                student.save()
                return HttpResponseRedirect('/home')
            else:
                return HttpResponse("old Password Not Matched")