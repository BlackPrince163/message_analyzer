from rest_framework import serializers
from .models import Message
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class MessageSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    status = serializers.CharField(source='get_status_display')
    class Meta:
        model = Message
        fields = '__all__'
