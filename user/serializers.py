
from re import search
from rest_framework import serializers
from .models import User

class UserRegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style = {"input_type": "password"}, write_only = True)
    class Meta:
        model = User
        fields = [
            'email',
            'name',
            'password',
            'password2',
            'tc',
        ]
        extra_kwargs = {
            'password':{'write_only':True}
        }
    
    def validate(self, args):
        email = args.get('email')
        password = args.get('password')
        password2 = args.get('password2')

        if User.objects.filter(email = email):
            raise serializers.ValidationError('Email already exist')
        if password != password2:
            raise serializers.ValidationError('Password and Confirm Password does not match !!')
        return args
    
    def create(self, validate_data):
        return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length = 255)
    class Meta:
        model = User
        fields = [
            'email',
            'password',
        ]

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'email',
            'name'
        ]