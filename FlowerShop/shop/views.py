from django.shortcuts import render, redirect
from .models import Customer, Flower, Purchase
from .forms import PurchaseForm, CustomerForm

def purchase_flower(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['customer']
            flower = form.cleaned_data['flower']
            Purchase.objects.create(customer=customer, flower=flower)
            return redirect('success')
    else:
        form = PurchaseForm()
    return render(request, 'shop/purchase_flower.html', {'form': form})

def display_purchases(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.cleaned_data['customer']
            purchases = Purchase.objects.filter(customer=customer)
            return render(request, 'shop/display_purchases.html', {'purchases': purchases, 'customer': customer})
    else:
        form = CustomerForm()
    return render(request, 'shop/select_customer.html', {'form': form})

def success(request):
    return render(request, 'shop/success.html')
