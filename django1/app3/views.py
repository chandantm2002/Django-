from django.shortcuts import render
from app2.forms import inputform

def home(request):
    if request.method == "POST":
        form1 = inputform(request.POST)
        if form1.is_valid():
            data = form1.cleaned_data
            n1 = data.get("input1")
            result = getFact(n1)
            return render(request, "app3/index.html", {'param1': result, 'form': form1})
    else:
        form1 = inputform()
    return render(request, "app3/index.html", {'form': form1})

def fact(n1):
    fact1 = 1
    for i in range(1, n1 + 1):
        fact1 *= i
    return fact1

def getFact(limit1):
    list1 = []
    list2 = []
    for i in range(2, limit1 + 1):
        list1.append(fact(i))
        list2.append(i)
    return zip(list1, list2)
