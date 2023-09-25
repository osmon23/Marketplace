from django.urls import  path
from rest_framework import routers


from .views import AboutUsListView, ContactsListView

router = routers.DefaultRouter()


urlpatterns = [
    path('', AboutUsListView.as_view(), name='about_us'),
    path('contacts/', ContactsListView.as_view(), name='contacts'),
] + router.urls


# router.register(r'', AboutUsViewSet, basename='about_us')
# router.register(r'images', AboutUsImageViewSet, basename='about_us_images')
# router.register(r'videos', AboutUsVideoViewSet, basename='about_us_videos')

# urlpatterns = router.urls
