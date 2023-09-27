from django.urls import path
from rest_framework import routers

from .views import ArticlesViewSet, NewsListView, NewsDetailView

router = routers.DefaultRouter()

router.register(r'articles', ArticlesViewSet, basename='articles')


urlpatterns = [
    path("news-list", NewsListView.as_view(), name="news-list"),
    path("news-detail/<int:pk>", NewsDetailView.as_view(), name="news-detail"),
] + router.urls
