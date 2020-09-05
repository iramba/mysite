# chat/consumers.py
from . import consumers

import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        print('==============')
        print(text_data)
        print('==============')
        text_data_json = json.loads(text_data)
        customerId = text_data_json['id']
        image = text_data_json['image']
        items = text_data_json['items']

        # Send id to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'id': customerId,
                'image': image,
                'items': items
            }
        )  # Receive id from room group

    async def chat_message(self, event):
        customerId = event['id']
        image = event['image']
        items = event['items']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'id': customerId,
            'image': image,
            'items': items
        }))
