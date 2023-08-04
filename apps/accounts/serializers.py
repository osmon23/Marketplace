from rest_framework import serializers

from .models import CustomUser, Seller


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,)

    class Meta:
        model = CustomUser
        fields = (
            'id',
            'email',
            'username',
            'password',
            'phone_number',
            'photo',
            'address',
            'birthday',
            'job',
            'specialization',
            'whatsapp',
            'telegram',
            'role'
        )
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


class SellerSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True,)

    class Meta:
        model = Seller
        fields = (
            'id',
            'email',
            'username',
            'password',
            'phone_number',
            'photo',
            'address',
            'birthday',
            'job',
            'specialization',
            'whatsapp',
            'telegram',
            'role'
        )
    
    def create(self, validated_data):
        user = Seller.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user
