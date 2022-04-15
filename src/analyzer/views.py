from django.db.models.signals import post_save
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Message
from .serializers import MessageSerializer, CreateMessageSerializer


class MessageListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Message.objects.all().order_by('id')
    serializer_class = MessageSerializer


class MessageCreateView(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Message.objects.all()
    serializer_class = CreateMessageSerializer
    from .service import signals
    post_save.connect(signals.start_listener)


class UpdateStatusMessageView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, *args, **kwargs):
        pk = int(request.data['message_id'])
        if not pk:
            return Response({"error": "Method PUT not allowed"})
        Message.objects.filter(pk=pk).update(status=2 if request.data["success"] == 'True' else 3)
        return Response({"post": request.data})