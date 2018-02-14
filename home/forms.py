from django import forms



class PayFeesForm(forms.Form):
    # stu_roll = forms.IntegerField(label="stu_roll")
    stu_semester = forms.CharField(label="stu_semester",max_length=50)
    paid_amount = forms.IntegerField(label="paid_amount")
    receipt_no = forms.CharField(label="receipt_no",max_length=300)
    remarks = forms.CharField(label="remarks",max_length=150)