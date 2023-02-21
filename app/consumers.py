import json
from channels.generic.websocket import AsyncWebsocketConsumer 
from asgiref.sync import async_to_sync
from time import sleep

class NotificationConsumer(AsyncWebsocketConsumer):
    
    async def connect(self):
        print("==================")
        await self.accept() 
        await self.channel_layer.group_add("notification_group", self.channel_name)
         
         
    async def disconnect(self, close_code): 
        pass
    # Receive message from WebSocket
    async def receive(self, text_data):
        print(text_data)
        await self.channel_layer.group_send(
            'notification_group',
            {
                'type':'send.msg',
                'msg':'thank for connecting'
            }
            )
    async def send_videonofication(self,event):
        await  self.send(event['msg'])

    async def send_msg(self,event):
        print(event['msg'])
        await  self.send(event['msg'])
    async def chat_message(self, event):
        print(event['message'])
        await self.send(json.dumps("Total Online :- "+str(event['message'])))
         


