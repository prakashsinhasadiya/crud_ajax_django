from django import forms
from crud.models import Student

class StudentForm(forms.ModelForm):
    name = forms.CharField(label='Your name',max_length=100)
    city = forms.CharField(label='Your city',max_length=100)
    number = forms.CharField(label='Your number',max_length=100)

    class Meta:
        model = Student
        fields = ['name','city','number']