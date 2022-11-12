# chat/urls.py
from django.urls import path

from .views import chat_view

urlpatterns = [
     path('', chat_view.index, name='index'),
     path('<str:room_name>/', chat_view.room, name='room'),
]