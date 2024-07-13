from django.shortcuts import render
from app2.forms import inputform
def home(request):
    if request.method=="POST":
        form1=inputform(request.POST)
        if form1.is_valid():
            data=form1.cleaned_data
            n1=data.get("input1")
            result=fact(n1)
            return render(request,"app2/index.html",{'param1':result, 'param2':n1, 'form':form1})
    else:
        form1=inputform()  
    return render(request,"app2/index.html",{'form':form1})

def fact(n1):  
    fact1=1
    for i in range(1,n1+1,1):
        fact1=fact1*i
    return fact1
