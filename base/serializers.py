from rest_framework import serializers
from .models import Todo
from api.serializers import UserSerializer

class TodoSerializer(serializers.ModelSerializer):
    creator_detail = UserSerializer(source = 'creator', read_only = True)
    class Meta:
        model = Todo
        fields = [
            'pk',
            'creator_detail',
            'title',
            'body',
            'is_completed',
            'created_at'
        ]
        