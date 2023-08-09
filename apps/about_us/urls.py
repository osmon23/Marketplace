from django.urls import  path

from .views import AboutUsListView

urlpatterns = [
    path('', AboutUsListView.as_view(), name='about_us'),
]

'''
если понадобится crud на будущее при использовании viewsets
'''
# from rest_framework import routers

# router = routers.DefaultRouter()

# router.register(r'', AboutUsViewSet, basename='about_us')
# router.register(r'images', AboutUsImageViewSet, basename='about_us_images')
# router.register(r'videos', AboutUsVideoViewSet, basename='about_us_videos')

# urlpatterns = router.urls
