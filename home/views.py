from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
from home.models import PayFees , Result
from user.models import Student , Branch , Semester , Course
from home.forms import PayFeesForm
from user.forms import ProfilePicForm
from reportlab.pdfgen import canvas
from django.core.files.storage import FileSystemStorage

def home(request):
    global semester
    if 'stu_roll' not in request.session:
        return HttpResponseRedirect('/user/login')
    else:
        stu = Student.objects.filter(stu_roll = request.session['stu_roll'] )
        for stud in stu:
            semester = Semester.objects.filter(id=stud.stu_semester_id)
        student = {
            "student" : stu,
            "semesters" : semester
        }
        return render(request , 'home.html' , student)

def profile(request):
    global branch, course, semester
    if 'stu_roll' not in request.session:
        return HttpResponseRedirect('/user/login')
    else:
        student = Student.objects.filter(stu_roll = request.session['stu_roll'])
        for stu in student:
            branch = Branch.objects.filter(id = stu.stu_branch_id)
            course = Course.objects.filter(id = stu.stu_course_id)
            semester = Semester.objects.filter(id = stu.stu_semester_id)
        student  = {
           "student": student,
           "branch": branch,
           "course": course,
           "semester": semester
        }
        return render(request ,"profile.html" , student)
def payFees(request):
    if 'stu_roll' not in request.session:
        return HttpResponseRedirect('/user/login')
    else:
        form = PayFeesForm()
        if request.method == "POST":
            form = PayFeesForm(request.POST)
            print(form.errors)
            if form.is_valid():
                fees = PayFees()
                fees.stu_roll = request.session['stu_roll']
                fees.stu_semester = form.cleaned_data['stu_semester']
                fees.paid_amount = form.cleaned_data['paid_amount']
                fees.receipt_no = form.cleaned_data['receipt_no']
                fees.remarks = form.cleaned_data['remarks']
                fees.save()
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="feesFile.pdf"'
                p = canvas.Canvas(response)
                p.setFont("Helvetica", 20)
                p.drawString(20, 700, "National Institute of Technology,Kurukshetra" )
                p.setFont("Helvetica", 14)
                p.drawString(100, 650, "Fees ID : " + str(fees.id))
                p.drawString(300, 650, "Student Roll : " +str(fees.stu_roll))
                p.drawString(100, 620, "Semester : "+str(fees.stu_semester))
                p.drawString(300, 620, "Receipt No : "+str(fees.receipt_no))
                p.drawString(100, 590, "Remarks : "+str(fees.remarks))
                p.showPage()
                p.save()
                return response
        else:
            stu = Student.objects.filter(stu_roll=request.session['stu_roll'])
            sem = Semester.objects.all()
            student = {
                "student": stu,
                "semesters": sem
            }
            return render(request, 'pay.html', student)


def result(request):
    global semester
    if 'stu_roll' not in request.session:
        return HttpResponseRedirect('/user/login')
    else:
        res = Result.objects.filter(stu_roll= request.session['stu_roll'])
        stu = Student.objects.filter(stu_roll=request.session['stu_roll'])
        for stud in stu:
            semester = Semester.objects.filter(id=stud.stu_semester_id)
        student = {
            "student": stu,
            "semesters": semester,
            "result": res
        }
        return render(request , 'result.html' , student)

def profile_pic_upload(request):
    saved = False
    if request.method == "POST" and request.FILES['profile_pic']:

        profile_pic = request.FILES['profile_pic']
        fs = FileSystemStorage()
        filename = fs.save(profile_pic.name, profile_pic)
        uploaded_file_url = fs.url(filename)
        student = Student.objects.get(stu_roll=request.session['stu_roll'])
        print(uploaded_file_url)
        student.stu_image_url = uploaded_file_url
        print(uploaded_file_url)
        student.save()
        saved = True
        return HttpResponseRedirect('/home/profile')
    else:
         return HttpResponse("Some Error Occured")
