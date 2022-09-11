from django.contrib.auth.decorators import login_required

from .views import show_message
from django.urls import path

urlpatterns = [
    path('dialogs/',login_required(show_message.DialogsView.as_view()),name='dialogs'),
    path('dialogs/create/<int:user_id>', login_required(show_message.CreateDialogView.as_view()), name='create_dialog'),
    path('dialogs/<int:chat_id>', login_required(show_message.MessagesView.as_view()), name='messages'),
]

