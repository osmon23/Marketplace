from django.urls import path
from .views import ChatListAPIView, ChatRetrieveAPIView, chat_room

urlpatterns = [
    path('', ChatListAPIView.as_view(), name='chats'),
    path('room/<int:pk>/', ChatRetrieveAPIView.as_view(), name='chat_room'),
    path('<int:room_id>/', chat_room, name='room'),
]
