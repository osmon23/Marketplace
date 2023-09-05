from django.urls import  path
from rest_framework import routers


from .views import AboutUsListView, ContactsViewSet

router = routers.DefaultRouter()

router.register(r'contacts', ContactsViewSet, basename='contacts')

urlpatterns = [
    path('', AboutUsListView.as_view(), name='about_us'),
] + router.urls


# router.register(r'', AboutUsViewSet, basename='about_us')
# router.register(r'images', AboutUsImageViewSet, basename='about_us_images')
# router.register(r'videos', AboutUsVideoViewSet, basename='about_us_videos')

# urlpatterns = router.urls
