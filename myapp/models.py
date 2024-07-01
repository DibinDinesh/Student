from django.db import models

# Create your models here.

class Student(models.Model):

    id=models.PositiveIntegerField(primary_key=True)

    student_name=models.CharField(max_length=200)

    course_name=models.CharField(max_length=200)

    fees=models.PositiveIntegerField()

    def __str__(self):

        return self.student_name

