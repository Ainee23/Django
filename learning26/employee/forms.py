from django import forms
from .models import Employee,Course,Student,Car

#employee form
#modelForm -->it will create form using model fileds
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' #[name,age,salary,joiningDate,post]

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
    
class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'