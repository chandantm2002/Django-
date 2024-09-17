from django.urls import path
from .views import voting_data

urlpatterns = [
    path('voting/', voting_data, name='voting_data'),
]

