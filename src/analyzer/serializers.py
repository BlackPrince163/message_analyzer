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


class CreateMessageSerializer(serializers.ModelSerializer):
    message = serializers.CharField(source='content')
    user_id = serializers.SlugRelatedField(
        source='user',
        queryset=User.objects.all(),
        write_only=True,
        slug_field="id"
    )

    class Meta:
        model = Message
        fields = ['user_id', 'message']



class UpdateStatusMessageSerializer(serializers.Serializer):
    message_id = serializers.IntegerField()
    success = serializers.BooleanField()
