from django.urls import path
from .views import purchase_flower, display_purchases, success

urlpatterns = [
    path('purchase/', purchase_flower, name='purchase_flower'),
    path('display/', display_purchases, name='display_purchases'),
    path('success/', success, name='success'),
]
