from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
from home.models import PayFees
from user.models import Student
from home.forms import PayFeesForm
from reportlab.pdfgen import canvas
from reportlab.platypus import Image
import os,random
# Create your views here.

def home(request):
    if 'stu_roll' not in request.session:
        return HttpResponseRedirect('/user/login')
    else:
        stu = Student.objects.filter(stu_roll = request.session['stu_roll'] )
        student = {
            "student" : stu,
            "semesters" : {
                "Sem 1",
                "Sem 2",
                "Sem 3",
                "Sem 4",
                "Sem 5",
                "Sem 6",
                "Sem 7",
                "Sem 8"
            }
        }
        return render(request , 'home.html' , student)

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


                # return HttpResponseRedirect('/home')