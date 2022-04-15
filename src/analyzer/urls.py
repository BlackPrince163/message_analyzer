from django.urls import path

from .views import MessageListView, MessageCreateView, UpdateStatusMessageView

urlpatterns = [
    path('v1/message/all', MessageListView.as_view()),
    path('v1/message', MessageCreateView.as_view()),
    path('v1/message_confirmation', UpdateStatusMessageView.as_view()),
]
