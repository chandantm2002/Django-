
from django.urls import path
from .views import CustomerListView, FurnitureDetailView

urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path('furniture/<int:pk>/', FurnitureDetailView.as_view(), name='furniture-detail'),
]
