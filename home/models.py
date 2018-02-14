from django.db import models

# Create your models here.

class PayFees(models.Model):
    stu_roll = models.IntegerField()
    stu_semester = models.CharField(max_length=50, default="")
    paid_amount = models.IntegerField(default="0")
    receipt_no = models.CharField(max_length=300)
    remarks = models.CharField(max_length=150 ,default="")
    class Meta:
        db_table = "payfees"