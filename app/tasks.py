from celery import shared_task
import requests
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import random
import json
from app.models import Post
import datetime  
channel_layer = get_channel_layer()
 


@shared_task
def send_notification_user():
    
    # if len(get_video) !=0:

   
    
    print("=================")

