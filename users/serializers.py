
from rest_framework import serializers
from .models import User

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'full_name', 'password', 'phone_number', 'billing_address', 'shipping_address', 'user_type')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            full_name=validated_data['full_name'],
            phone_number=validated_data.get('phone_number', ''),
            billing_address=validated_data.get('billing_address', ''),
            shipping_address=validated_data.get('shipping_address', ''),
            user_type=validated_data.get('user_type', 'customer')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'full_name', 'phone_number', 'billing_address', 'shipping_address', 'user_type')
