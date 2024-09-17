from django.shortcuts import render
from .forms import CityForm
from .models import City

def index(request):
    selected_city = None
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            selected_city = form.cleaned_data['city']
    else:
        form = CityForm()
    
    context = {
        'form': form,
        'selected_city': selected_city
    }
    return render(request, 'clocks/index.html', context)
