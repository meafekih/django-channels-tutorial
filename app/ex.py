import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from channels.db import database_sync_to_async
from django.contrib.auth.models import User
import redis

class ChatConsumer(AsyncWebsocketConsumer):

    def verify_redis(self):
        try:
            client = redis.StrictRedis(host='localhost', port=6379, db=0)
            response = client.ping()
            if response:
                print("Redis server is running and accessible.")
            else:
                print("Redis server is not responding.")
        except redis.ConnectionError:
            print("Could not connect to the Redis server.")
    
    async def connect(self):
        self.verify_redis()
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope["user"]

        if user.is_authenticated:
            await self.save_message(user, message)
            await self.send_message(message, user.username)

    async def send_message(self, message, username):
        await self.send(text_data=json.dumps({'message': message,'username': username,}))

    async def save_message(self, user, content):
        await Message.objects.create(user=user, content=content)

# function 