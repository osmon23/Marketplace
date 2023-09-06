from django.urls import path
from rest_framework import routers

from .views import ArticlesViewSet, NewsListView, NewsDetailView

router = routers.DefaultRouter()

router.register(r'articles', ArticlesViewSet, basename='articles')


urlpatterns = [
    path("news-list", NewsListView.as_view(), name="news-list"),
    path("news-detail/<int:pk>", NewsDetailView.as_view(), name="news-detail"),
    # path("articles-list", views.ArticlesListView.as_view(), name="articles-list"),
    # path("articles-detail/<int:pk>", views.ArticlesDetailView.as_view(), name="articles-detail"),
] + router.urls
