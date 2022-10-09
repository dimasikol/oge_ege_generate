from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone


class Chat(models.Model):
    DIALOG = 'D'
    CHAT = 'C'
    CHAT_TYPE_CHOICE = ((DIALOG,'Dialog'), (CHAT,'Chat'))
    type = models.CharField(max_length=1,choices=CHAT_TYPE_CHOICE,default=DIALOG)
    members = models.ManyToManyField(User)

    def get_absolute_url(self):
        return 'user:messages', (), {'chat_id': self.pk}


class Message(models.Model):
    chat = models.ForeignKey(Chat,on_delete=models.DO_NOTHING,related_name='chat')
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='author')
    message = RichTextUploadingField()
    pub_date = models.DateTimeField(default=timezone.now(),blank=True)
    is_readed = models.BooleanField(default=False)


    class META:
        ordering = ['-pub_date','-is_readed',]