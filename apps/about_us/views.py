from django.shortcuts import render

from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response

from .models import AboutUs, AboutUsImage, AboutUsVideo
from .serializers import AboutUsSerializer, AboutUsImageSerializer, AboutUsVideoSerializer


class AboutUsListView(generics.ListAPIView):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        about_us_data = []
        for item in serializer.data:
            about_us_item = item.copy()
            about_us_id = about_us_item['id']

            images_queryset = AboutUsImage.objects.filter(about_us_id=about_us_id)
            images_serializer = AboutUsImageSerializer(images_queryset, many=True)

            videos_queryset = AboutUsVideo.objects.filter(about_us_id=about_us_id)
            videos_serializer = AboutUsVideoSerializer(videos_queryset, many=True)

            about_us_item['images'] = images_serializer.data
            about_us_item['videos'] = videos_serializer.data

            about_us_data.append(about_us_item)

        return Response(about_us_data)


'''
если понадобится crud на будущее
'''
# class AboutUsViewSet(viewsets.ModelViewSet):
#     queryset = AboutUs.objects.all()
#     serializer_class = AboutUsSerializer
#     permission_classes = [permissions.IsAdminUser, permissions.DjangoModelPermissionsOrAnonReadOnly]


# class AboutUsImageViewSet(viewsets.ModelViewSet):
#     queryset = AboutUsImage.objects.all()
#     serializer_class = AboutUsImageSerializer
#     permission_classes = [permissions.IsAdminUser, permissions.DjangoModelPermissionsOrAnonReadOnly]


# class AboutUsVideoViewSet(viewsets.ModelViewSet):
#     queryset = AboutUsVideo.objects.all()
#     serializer_class = AboutUsVideoSerializer
#     permission_classes = [permissions.IsAdminUser, permissions.DjangoModelPermissionsOrAnonReadOnly]
