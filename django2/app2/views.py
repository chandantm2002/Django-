from django.shortcuts import render
from app2.forms import InputForm

def home(request):
    if request.method == "POST":
        form = InputForm(request.POST)
        if form.is_valid():
            form.save()  # save to database
            return render(request, 'app2/index.html', {'form': form, 'param1': "Success"})
    else:
        form = InputForm()
    return render(request, 'app2/index.html', {'form': form})
