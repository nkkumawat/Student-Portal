from django.db import models

# Create your models here.

class Student(models.Model):
    stu_name = models.CharField(max_length=150)
    stu_mail = models.CharField(max_length=150, default="")
    stu_address = models.CharField(max_length=300,default="")
    stu_password = models.CharField(max_length=300 )
    stu_mobile = models.IntegerField(default="")
    stu_roll = models.IntegerField()
    class Meta:
        db_table = "student"