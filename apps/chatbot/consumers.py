import json
import datetime

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.auth import get_user

from .models import Message, Chat
import logging

logger = logging.getLogger(__name__)

class ChatConsumer(AsyncWebsocketConsumer):
    @sync_to_async
    def get_chat(self, room_id, user):
        chat, created = Chat.objects.get_or_create(id=room_id)
        chat.participants.add(user)
        return chat
    
    @sync_to_async
    def create_message(self, chat, user, message):
        message = Message.objects.create(
            chat=chat,
            sender=user,
            content=message
        )

    async def connect(self):
        user = await get_user(self.scope)

        if user.is_authenticated:
            self.room_id = self.scope['url_route']['kwargs']['room_id']

            chat = await self.get_chat(self.room_id, user)
            if not chat:
                await self.close()
                logger.error(f"Failed to connect: Chat not found for room_id {self.room_id}")
                return

            self.room_group_name = f"chat_{self.room_id}"

            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            await self.accept()
        else:
            await self.close()
            logger.error("Failed to connect: User is not authenticated")

    async def disconnect(self, close_code):
        if hasattr(self, 'room_group_name'):
            await self.channel_layer.group_discard(
                self.room_group_name,
                self.channel_name
            )
        print('=' * 50, 'disconnect', '=' * 50)

    async def receive(self, text_data):
        user = await get_user(self.scope)
        data = json.loads(text_data)
        message = data['message']
        print('=' * 50, data, '=' * 50, message)

        chat = await self.get_chat(self.room_id, user)

        await self.create_message(chat, user, message)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'sender_id': user.username,
                'timestamp': datetime.datetime.now().isoformat(),
            }
        )

    async def chat_message(self, event):
        await self.send(text_data=json.dumps(event))
        print('=' * 50, event, '=' * 50)
