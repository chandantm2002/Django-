from django.urls import path
from .views import highlight_words

urlpatterns = [
    path('<str:words>/', highlight_words, name='highlight_words'),
]
