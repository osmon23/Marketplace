from django.contrib import admin
from .models import Chat, Message


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'participants',
        'created_at',
    )
    list_display_links = (
        'participants',
    )
    search_fields = (
        'participants__username',
        'participants__email',
    )


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'chat',
        'sender',
    )
    list_display_links = (
        'chat',
        'sender',
    )
    search_fields = (
        'chat__participants__username',
        'chat__participants__email',
        'sender__username',
        'sender__email',
        'content',
    )
