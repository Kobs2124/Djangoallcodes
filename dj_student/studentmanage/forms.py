from django import forms
from .models import Student



class SevenDigitIntegerField(forms.IntegerField):
    def validate(self, value):
        super().validate(value)
        if value is not None:
            if len(str(value)) != 7:
                raise forms.ValidationError("Student Number only accepts 7 digits")

class StudentForm(forms.ModelForm):
    student_num = SevenDigitIntegerField(min_value=1000000, max_value=9999999)
    gpa = forms.DecimalField(max_digits=3, decimal_places=2, min_value=1.0, max_value=5.0)

    class Meta:
        model = Student
        fields = ['student_num', 'f_name', 'l_name', 'email', 'field_of_study', 'gpa']
        labels = {
            'student_num': 'Student Number',
            'f_name': 'First Name',
            'l_name': 'Last Name',
            'email': 'Email', 
            'field_of_study': 'Field of Study',
            'gpa': 'GPA'
        }
        widgets = {
            'student_num': forms.NumberInput(attrs={'class': 'form-control'}),
            'f_name': forms.TextInput(attrs={'class': 'form-control'}),
            'l_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_student_num(self):
        student_num = self.cleaned_data['student_num']
        if Student.objects.filter(student_num=student_num).exists():
            raise forms.ValidationError("Student Number Already Exist!")
        return student_num
    



# class SevenDigitIntegerField(forms.IntegerField):
#     def validate(self, value):
#         super().validate(value)
#         if value is not None:
#             if len(str(value)) != 7:
#                 raise forms.ValidationError("Student Number only accepts 7 digits")

# class StudentForm(forms.ModelForm):
#     student_num = SevenDigitIntegerField(min_value=1000000, max_value=9999999)
#     gpa = forms.DecimalField(max_digits=3, decimal_places=2, min_value=1.0, max_value=5.0)

#     class Meta:
#         model = Student
#         fields = ['student_num', 'f_name', 'l_name', 'email', 'field_of_study', 'gpa']
#         labels = {
#             'student_num': 'Student Number',
#             'f_name': 'First Name',
#             'l_name': 'Last Name',
#             'email': 'Email', 
#             'field_of_study': 'Field of Study',
#             'gpa': 'GPA'
#         }
#         widgets = {
#             'student_num': forms.NumberInput(attrs={'class': 'form-control'}),
#             'f_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'l_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#             'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
#             'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
#         }

 
