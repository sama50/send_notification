from django.db import models
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
# Create your models here.
import json
channel_layer = get_channel_layer()


class Post(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media')
    upload_time = models.DateTimeField(default=False)

    def save(self, *args, **kwargs):
        obj = super(Post, self).save(*args, **kwargs) # Call the real save() method
        print(self.id)

        async_to_sync(channel_layer.group_send)('notification_group',{
            'type':'send.videonofication',
            'msg': str(self.id)
            }) 
