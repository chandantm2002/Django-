from django.urls import path
from .views import insert_sample_channels, update_viewers, delete_channel, search_channels

urlpatterns = [
    path('insert/', insert_sample_channels, name='insert_sample_channels'),
    path('update/', update_viewers, name='update_viewers'),
    path('delete/', delete_channel, name='delete_channel'),
    path('search/', search_channels, name='search_channels'),
]
