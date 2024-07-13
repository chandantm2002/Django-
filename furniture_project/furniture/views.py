# furniture/views.py

from django.views.generic import ListView, DetailView
from .models import Customer, Furniture

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'

class FurnitureDetailView(DetailView):
    model = Furniture
    template_name = 'furniture_detail.html'
    context_object_name = 'furniture'
