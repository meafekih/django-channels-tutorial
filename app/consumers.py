import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import Message
from .views import get_user

class ChatRoomConsumer(AsyncWebsocketConsumer):

    async def new_message(self, data):           
        user_contact = await get_user(data["username"])  
        print(type(user_contact))
        message = Message.objects.create(user=user_contact, content=data['message'])
        message.save()
    
    commands = {
            'new_message': new_message
        }


    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        msg = text_data_json["message"]
        username = text_data_json["username"]
        #self.commands['new_message'](self, text_data_json)
        self.new_message(text_data_json)
        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "chatbox_message",
                "message": msg,
                "username": username,
            },
        )
        


    async def connect(self):
        self.chat_box_name = self.scope["url_route"]["kwargs"]["chat_box_name"]
        self.group_name = "chat_%s" % self.chat_box_name
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()
        print('chat box name: ' + self.chat_box_name)
        print('group name: '+ self.group_name)
        print('channel name: '+ self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def chatbox_message(self, event):
        message = event["message"]
        username = event["username"]

        await self.send(
            text_data=json.dumps(
                {
                    "message": message,
                    "username": username,
                }
            )
        )

