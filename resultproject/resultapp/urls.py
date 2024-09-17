from django.urls import path
from .views import index, get_results

urlpatterns = [
    path('', index, name='index'),
    path('get_results/', get_results, name='get_results'),
]
