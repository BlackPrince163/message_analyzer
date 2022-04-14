from rest_framework.response import Response
from rest_framework import generics

from .models import Message
from .serializers import MessageSerializer, CreateMessageSerializer


class MessageListView(generics.ListAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer


# class UpdateStatusMessageView(generics.GenericAPIView):
#     pass