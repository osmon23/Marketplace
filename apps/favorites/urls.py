from django.urls import path
from .views import AddToFavoriteView, RemoveFromFavoriteView, FavoriteItemsListView

urlpatterns = [
    path('add-to-favorite/', AddToFavoriteView.as_view(), name='add-to-favorite'),
    path('remove-from-favorite/<int:pk>/', RemoveFromFavoriteView.as_view(), name='remove-from-favorite'),
    path('favorite-items-list', FavoriteItemsListView.as_view(), name='favorite-items-list'),
]
