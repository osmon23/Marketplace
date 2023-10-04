from rest_framework import generics, permissions, viewsets
from rest_framework.generics import ListAPIView

from .permissions import IsAdminOrSellerOrReadOnly
from .models import News, Article
from .serializers import NewsSerializer, ArticleSerializer
from ..accounts.constants import Role


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.AllowAny]


class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.AllowAny]


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminOrSellerOrReadOnly]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['request'] = self.request
        return context

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class SellerArticlesListView(ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [IsAdminOrSellerOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            queryset = Article.objects.none()
        else:
            queryset = Article.objects.filter(created_by=user)
        return queryset
