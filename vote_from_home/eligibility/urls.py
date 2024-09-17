from django.urls import path
from .views import check_eligibility

urlpatterns = [
    path('<int:age>/', check_eligibility, name='check_eligibility'),
]
