from django import forms


class StudentForm(forms.Form):


    id=forms.IntegerField()

    student_name=forms.CharField()

    course_name=forms.CharField()

    fees=forms.IntegerField()

    
