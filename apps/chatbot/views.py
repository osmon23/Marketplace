from django.shortcuts import render
from django.contrib.auth.views import LoginView


def chat_room(request, room_id):
    return render(request, 'chat_room.html', {'room_id': room_id})
