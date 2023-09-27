from rest_framework import serializers

from .models import News, Article


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            'name',
            'description',
            'photo',
        )


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            'title',
            'description',
            'photo',
        )
