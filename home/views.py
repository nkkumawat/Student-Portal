from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
from home.models import PayFees , Result , Notification
from user.models import Student , Branch , Semester , Course
from home.forms import PayFeesForm
from reportlab.pdfgen import canvas
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
from django.core.files.storage import FileSystemStorage

def home(request):
    global semester
    if 'stu_roll' not in request.session:
        return HttpResponseRedirect('/user/login')
    else:
        stu = Student.objects.get(stu_roll = request.session['stu_roll'])
        semester = Semester.objects.get(id=stu.stu_semester_id)
        notification = Notification.objects.all()[: 8]
        student = {
            "student" : stu,
            "semesters" : semester,
            "notification": notification
        }
        return render(request , 'home.html' , student)

def profile(request):
    global branch, course, semester
    if 'stu_roll' not in request.session:
        return HttpResponseRedirect('/user/login')
    else:
        student = Student.objects.get(stu_roll = request.session['stu_roll'])
        # for stu in student:
        branch = Branch.objects.get(id = student.stu_branch_id)
        course = Course.objects.get(id = student.stu_course_id)
        semester = Semester.objects.get(id = student.stu_semester_id)
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
            fees = PayFees.objects.filter(stu_roll=request.session['stu_roll'] , stu_semester=form.cleaned_data['stu_semester'])
#            if fees:
                
            if form.is_valid():
                fees = PayFees()
                fees.stu_roll = request.session['stu_roll']
                fees.stu_semester = form.cleaned_data['stu_semester']
                fees.paid_amount = form.cleaned_data['paid_amount']
                fees.receipt_no = form.cleaned_data['receipt_no']
                fees.remarks = form.cleaned_data['remarks']
                fees.save()
                student = Student.objects.get(stu_roll = fees.stu_roll)
                response = HttpResponse(content_type='application/pdf')
                response['Content-Disposition'] = 'attachment; filename="feesFile.pdf"'
                p = canvas.Canvas(response)
                logo = ImageReader('./static/images/nit.png')
                p.drawImage(logo, 40, 700,width=100, height=100 , mask='auto')
                p.setFont("Helvetica", 20)
                p.drawString(150, 750, "XYZ Institute of Anything, College Place  " )
                p.setFont("Helvetica", 14)

                p.drawString(50, 650, "Name : " + str(student.stu_name))
                p.drawString(300, 650, "Roll No. : " + str(student.stu_roll))
                p.drawString(50, 620, "Mobile No. : " + str(student.stu_mobile))
                p.drawString(300, 620, "Email : " + str(student.stu_mail))
                p.drawString(50, 590, "Branch : " + str(Branch.objects.get(id=student.stu_branch_id).stu_branch))
                p.drawString(300, 590, "Course : " + str(Course.objects.get(id=student.stu_course_id).stu_course))
                p.drawString(50, 560, "Semester : " + str(fees.stu_semester))

                p.drawString(50, 520, "Fees ID : " + str(fees.id))
                p.drawString(300, 520, "Receipt No : "+str(fees.receipt_no))
                p.drawString(50, 490, "Remarks : "+str(fees.remarks))
                p.showPage()
                p.save()
                return response
        else:
            stu = Student.objects.get(stu_roll=request.session['stu_roll'])
            sem = Semester.objects.all()
            fees = PayFees.objects.filter(stu_roll=request.session['stu_roll'])
            student = {
                "student": stu,
                "semesters": sem,
                "fees": fees
            }
            return render(request, 'pay.html', student)


def result(request):
    global semester
    if 'stu_roll' not in request.session:
        return HttpResponseRedirect('/user/login')
    else:
        res = Result.objects.filter(stu_roll= request.session['stu_roll'])
        stu = Student.objects.get(stu_roll=request.session['stu_roll'])
        semester = Semester.objects.filter(id=stu.stu_semester_id)
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
def notifications(request):
    global semester
    if 'stu_roll' not in request.session:
        return HttpResponseRedirect('/user/login')
    else:
        stu = Student.objects.get(stu_roll=request.session['stu_roll'])
        semester = Semester.objects.get(id=stu.stu_semester_id)
        notification = Notification.objects.all()
        student = {
            "student": stu,
            "semesters": semester,
            "notification": notification
        }
        return render(request, 'notification.html', student)
