from django.urls import path

from .views import MessageListView, MessageCreateView

urlpatterns = [
    path('message/all', MessageListView.as_view()),
    path('v1/message', MessageCreateView.as_view()),
    # path('/api/v1/message_confirmation'),
]
