from django.db import models

# Create your models here.
class Student(models.Model):
    student_num = models.PositiveIntegerField()
    f_name = models.CharField(max_length=50)
    l_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    gpa = models.FloatField()
    

    def __str__(self):
        return f'Student {self.student_num}: {self.f_name} {self.l_name}'