from django.shortcuts import render
from django.http import JsonResponse
from .models import Student
from .forms import USNForm

def index(request):
    form = USNForm()
    return render(request, 'resultapp/index.html', {'form': form})

def get_results(request):
    usn = request.GET.get('usn')
    student = Student.objects.get(usn=usn)
    results = student.results.all()
    results_data = [{
        'subject_code': result.subject_code,
        'subject_name': result.subject_name,
        'cie_marks': result.cie_marks,
        'see_marks': result.see_marks
    } for result in results]
    return JsonResponse({'student_name': student.name, 'results': results_data})
