from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MessageListView, MessageCreateView, UpdateStatusMessageView, test

router = DefaultRouter()
# router.register('v1/message_confirmation', UpdateStatusMessageView, '123')

urlpatterns = [
    path('', include(router.urls)),
    path('v1/message/all', MessageListView.as_view()),
    path('v1/message', MessageCreateView.as_view()),
    path('v1/message_confirmation', UpdateStatusMessageView.as_view()),
    path('test', test)
]
