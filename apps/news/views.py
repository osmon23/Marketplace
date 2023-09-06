
from rest_framework import generics, permissions, viewsets

from .permissions import IsStaffOrSellerOrReadOnly
from .models import News, Article
from .serializers import  NewsSerializer, ArticleSerializer


class NewsListView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.AllowAny]


class NewsDetailView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.AllowAny]


# class ArticlesListView(generics.ListAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [permissions.AllowAny]
#
#
# class ArticlesDetailView(generics.RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [permissions.AllowAny]

class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsStaffOrSellerOrReadOnly]
