from django.shortcuts import render

from rest_framework import generics, permissions

from .models import Chat
from .serializers import ChatSerializer, ChatDetailSerializer


class ChatListAPIView(generics.ListAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(participants=user)


class ChatRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatDetailSerializer
    lookup_field = 'pk'
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(participants=user)


def chat_room(request, room_id):
    return render(request, 'chat_room.html', {'room_id': room_id})
