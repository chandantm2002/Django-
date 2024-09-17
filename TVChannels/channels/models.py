from django.db import models

class Channel(models.Model):
    channel_name = models.CharField(max_length=100)
    channelnum = models.IntegerField()
    language = models.CharField(max_length=50)
    channeltype = models.CharField(max_length=50)
    number_of_viewers = models.IntegerField()

    def __str__(self):
        return self.channel_name
