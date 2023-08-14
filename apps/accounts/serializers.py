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
        if 'role' in validated_data:
            user_with_role = CustomUser.objects.create_user(
                email=validated_data['email'],
                username=validated_data['username'],
                password=validated_data['password'],
                role=validated_data['role'],
            )
            return user_with_role
        else:
            user = CustomUser.objects.create_user(
                email=validated_data['email'],
                username=validated_data['username'],
                password=validated_data['password'],
            )
            return user


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'email',
            'username',
            'phone_number',
            'photo',
            'address',
            'birthday',
            'job',
            'specialization',
            'whatsapp',
            'telegram',
            'role',
        )


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
            'role',
            'INN',
            'type',
            'certificate_number',
            'confirmation_code',
            'is_active',
        )
    
    def create(self, validated_data):
        user = Seller.objects.create_user(
            email=validated_data['email'],
            username=validated_data['username'],
            INN=validated_data['INN'],
            password=validated_data['password'],
        )
        return user


class SellerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = (
            'email',
            'username',
            'phone_number',
            'photo',
            'address',
            'birthday',
            'job',
            'specialization',
            'whatsapp',
            'telegram',
            'role',
            'INN',
            'type',
            'certificate_number',
            'confirmation_code',
            'is_active',
        )
