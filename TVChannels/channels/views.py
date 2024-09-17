from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Channel

def insert_sample_channels(request):
    Channel.objects.bulk_create([
        Channel(channel_name='Star Plus', channelnum=1, language='Hindi', channeltype='Entertainment', number_of_viewers=45),
        Channel(channel_name='Sony TV', channelnum=2, language='Hindi', channeltype='Entertainment', number_of_viewers=40),
        Channel(channel_name='National Geographic', channelnum=3, language='English', channeltype='Documentary', number_of_viewers=30),
        Channel(channel_name='Star Sports', channelnum=4, language='English', channeltype='Sports', number_of_viewers=60),
    ])
    return HttpResponse("Inserted 4 sample channels")

def update_viewers(request):
    Channel.objects.filter(channel_name__icontains='Star').update(number_of_viewers=50)
    return HttpResponse("Updated number_of_viewers to 50 for channels containing 'Star'")

def delete_channel(request):
    Channel.objects.filter(channelnum=3).delete()
    return HttpResponse("Deleted channel with number 3")

def search_channels(request):
    channels = Channel.objects.filter(number_of_viewers__gte=50, language='Hindi')
    return render(request, 'channels/search_results.html', {'channels': channels})
