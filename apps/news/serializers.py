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
    created_by = serializers.StringRelatedField(source='created_by.email')
    created_by_id = serializers.StringRelatedField(source='created_by.id')
    class Meta:
        model = Article
        fields = (
            'title',
            'description',
            'photo',
            'created_by',
            'created_by_id',
        )
