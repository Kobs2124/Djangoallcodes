from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Student
from .forms import StudentForm

def studenthomepage(request):
    search_query = request.GET.get('search')
    students = Student.objects.all()

    if search_query:
        students = students.filter(
            student_num__icontains=search_query
        ) | students.filter(
            field_of_study__icontains=search_query
        )

    return render(request, 'studentmanage/index.html', {'students': students})

def see_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('studenthomepage'))

def add(request):
    success = False  # Initialize the success flag
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to create a new student
            success = True  # Set success flag to True
        else:
            # Display an error message if the form is not valid
            error_message = form.errors
            return render(request, 'studentmanage/add.html', {'form': form, 'error_message': error_message})
    else:
        form = StudentForm()
    return render(request, 'studentmanage/add.html', {
        'form': form,
        'success': success  # Pass the success flag to the template
    })
