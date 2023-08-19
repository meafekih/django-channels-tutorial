import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import async_to_sync
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Message
import redis
from channels.db import database_sync_to_async



class ChatRoomConsumer(AsyncWebsocketConsumer):

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
    

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        msg = text_data_json["message"]
        user_name = text_data_json["username"]

        user = await self.get_user(user_name)
        if user and user.is_authenticated:
            await self.saving(user, msg)
            await self.send_message(user_name, msg)
        else:
            await self.close()
        
    async def connect(self):
        self.verify_redis()
        self.chat_box_name = self.scope["url_route"]["kwargs"]["chat_box_name"]
        self.group_name = "chat_%s" % self.chat_box_name
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def chatbox_message(self, event):
        message = event["message"]
        username = event["username"]
        value = json.dumps({"message": message,"username": username,})
        await self.send(text_data=value)

    @database_sync_to_async
    def get_user(self, user_name):
        return User.objects.get(username= user_name)

    @database_sync_to_async
    def saving(self, user, msg):
        Message.objects.create(user=user,content=msg)

    async def send_message(self, username, msg):
        await self.channel_layer.group_send(self.group_name,
            {"type": "chatbox_message","message": msg,"username": username,},)


