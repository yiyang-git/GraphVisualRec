# forms.py
from django import forms
from .models import JobFunction,UserForm

class JobFunctionForm(forms.ModelForm):
    class Meta:
        model = JobFunction
        fields = ['job_function_description']
        labels = {
            'job_function_description': '职位描述',
        }

class UserForm_form(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = ['email','password', 'name','gender','age','post', 'city','education','department'
                  ,'workenvironment','techSkillLevel','equipmentSkillLevel','experience_years']
        widgets = {
            'password': forms.PasswordInput(),  # 将密码字段设为密码输入框
        }
