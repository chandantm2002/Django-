from django.urls import path
from .views import registered_students

urlpatterns = [
    path('registered/', registered_students, name='registered_students'),
]
