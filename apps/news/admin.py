from django.contrib import admin

from .models import News, Article


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name', 'description',)
    list_filter = ('name', 'description',)
    ordering = ('name',)
    list_display_links = ('name',)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_by', 'description',)
    search_fields = ('title', 'description', 'created_by',)
    list_filter = ('title', 'description',)
    ordering = ('title',)
    list_display_links = ('title', 'created_by')