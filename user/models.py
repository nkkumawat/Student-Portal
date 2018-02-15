from django.db import models
# Create your models here.
class Student(models.Model):
    stu_name = models.CharField(max_length=150)
    stu_roll = models.IntegerField()
    stu_mail = models.CharField(max_length=150, default="")
    stu_address = models.CharField(max_length=300,default="")
    stu_password = models.CharField(max_length=300)
    stu_image_url = models.CharField(max_length=300,default="/static/images/nit.png")
    stu_branch_id = models.IntegerField(default="-1")
    stu_course_id = models.IntegerField(default="-1")
    stu_semester_id = models.IntegerField(default="-1")
    stu_mobile = models.IntegerField(default="")

    class Meta:
        db_table = "student"
class Branch(models.Model):
    stu_branch = models.CharField(max_length=150)
    class Meta:
        db_table = "branch"
class Course(models.Model):
    stu_course = models.CharField(max_length=50)
    class Meta:
        db_table = "course"
class Semester(models.Model):
    stu_semester = models.IntegerField();
    class Meta:
        db_table = "semester"