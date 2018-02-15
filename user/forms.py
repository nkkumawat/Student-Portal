from django import forms

class LoginForm(forms.Form):
    stu_roll = forms.CharField(label="stu_roll",max_length=100)
    stu_password = forms.CharField(label="stu_password" , max_length=100)
    # password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(forms.Form):
    stu_name = forms.CharField(label="stu_name", max_length=100)
    stu_mail = forms.CharField(label="stu_mail", max_length=100)
    stu_password = forms.CharField(label="stu_password", max_length=100)
    stu_mobile = forms.IntegerField(label="stu_mobile")
    stu_address = forms.CharField(label="stu_address", max_length=100)
    stu_roll = forms.IntegerField(label="stu_roll")
    stu_branch_id = forms.CharField(label="stu_branch_id" , max_length=100)
    stu_course_id = forms.CharField(label="stu_course_id" , max_length=100)
    stu_semester_id = forms.CharField(label="stu_semester_id" , max_length=100)

class ChangePasswordFrom(forms.Form):
    old_password = forms.CharField(label="old_password", max_length=100)
    new_password = forms.CharField(label="new_password", max_length=100)
    # password = forms.CharField(widget=forms.PasswordInput())
class ProfilePicForm(forms.Form):
    picture = forms.ImageField()






    # def cleaned_data(self):
    #     stu_name = self.cleaned_data.get("stu_name")
    #     stu_address = self.cleaned_data.get("stu_address")
    #     stu_roll = self.cleaned_data.get("stu_roll")
    #     stu_mobile = self.cleaned_data.get("stu_mobile")
    #     stu_mail = self.cleaned_data.get("stu_mail")
    #     stu_password = self.cleaned_data.get("stu_password")