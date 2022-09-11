from django.forms import ModelForm
from .models.message import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message']
        labels = {'message': ''}