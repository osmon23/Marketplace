from rest_framework import serializers

from .models import AboutUs, AboutUsImage, AboutUsVideo, Contacts


class AboutUsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsImage
        fields = ('image', )


class AboutUsVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUsVideo
        fields = ('video', )


class AboutUsSerializer(serializers.ModelSerializer):
    images = AboutUsImageSerializer(many=True, read_only=True)
    videos = AboutUsVideoSerializer(many=True, read_only=True)

    class Meta:
        model = AboutUs
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = (
            'id',
            'name',
            'value',
        )

