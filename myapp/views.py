from django.shortcuts import render,redirect

# Create your views here.
from django.views.generic import View

from myapp.models import Student

from myapp.forms import StudentForm

class StudentListView(View):

    def get(self,request,*args,**kwargs):

        qs=Student.objects.all()

        return render(request,"student_list.html",{"data":qs})

class StudentDetailsView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Student.objects.get(id=id)

        return render(request,"student_details.html",{"data":qs})

class StudentCreateView(View):

    def get(self,request,*args,**kwargs):
            
        form_instance=StudentForm()

        return render(request,"student_add.html",{"form":form_instance})
        
    def post(self,request,*args,**kwargs):
        
            form_instance=StudentForm(request.POST)

            if form_instance.is_valid():
                
                data=form_instance.cleaned_data

                Student.objects.create(**data)
                return redirect("student-list")
            else:
                return render(request,"student_add.html",{"form":form_instance})
        
class StudentDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Student.objects.get(id=id).delete()

        return redirect("student-list")




        
            
        

        
