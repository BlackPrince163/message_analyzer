from django.urls import path

from .views import MessageListView

urlpatterns = [
    path('message/all', MessageListView.as_view()),
]
