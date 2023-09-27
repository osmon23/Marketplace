from rest_framework import serializers

from .models import CustomUser, Seller, Wallet

from apps.stores.models import Store, Product


class WalletSerializer(serializers.ModelSerializer):
    seller_email = serializers.EmailField(source='seller.email', read_only=True)
    amount = serializers.ReadOnlyField()

    class Meta:
        model = Wallet
        fields = (
            'id',
            'amount',
            'seller_email',
        )


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = (
            'id',
            'name',
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
        )


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



