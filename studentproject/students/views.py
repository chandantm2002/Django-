from django.shortcuts import render
from .models import Student

def registered_students(request):
    students = Student.objects.filter(registered_or_not=True)
    context = {'students': students}
    return render(request, 'students/registered_students.html', context)
