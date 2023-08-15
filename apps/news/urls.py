from django.urls import path

from . import views

urlpatterns = [
    path("news-list", views.NewsListView.as_view(), name="news-list"),
    path("news-detail/<int:pk>", views.NewsDetailView.as_view(), name="news-detail"),
    path("articles-list", views.ArticlesListView.as_view(), name="articles-list"),
    path("articles-detail/<int:pk>", views.ArticlesDetailView.as_view(), name="articles-detail"),
]
