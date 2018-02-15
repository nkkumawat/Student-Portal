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


class Result(models.Model):
    stu_roll = models.IntegerField()
    stu_semester = models.IntegerField()
    stu_result = models.CharField(max_length=10)
    stu_sgpa = models.FloatField()
    stu_percent = models.FloatField()
    class Meta:
        db_table = "result"

class Notification(models.Model):
    notification_title = models.CharField(max_length=400)
    notification_attachment_url = models.CharField(max_length=400)
    notification_text = models.CharField(max_length=1000)
    class Meta:
        db_table = "notifications"