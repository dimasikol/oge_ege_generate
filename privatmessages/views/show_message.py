from django.db.models import Count
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from rest_framework import permissions
from ..models.message import Chat
from ..form import MessageForm
from rest_framework.views import APIView


class CreateDialogView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,user_id):
        chats = Chat.objects.filter(members__in=[request.user.id,user_id],type=Chat.DIALOG).annotate(c=Count('members')).filter(c=2)
        if chats.count() == 0:
            chat = Chat.objects.create()
            chat.members.add(request.user)
            chat.members.add(user_id)
        else:
            chat = chats.first()
        form = MessageForm(data=request.POST)
        #return render(request,'privatmessages/messages.html',context={'user_profile':request.user,'chat':chat,'form':MessageForm()})

        return redirect(reverse('messages',kwargs={'chat_id': chat.id}))


class DialogsView(View):
    def get(self, request):
        chats = Chat.objects.filter(members__in=[request.user.id])
        return render(request, 'privatmessages/dialogs.html', {'user_profile': request.user, 'chats': chats})


class MessagesView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,chat_id):
        try:

            chat = Chat.objects.get(id=chat_id)

            # if request.user in chat.members.all():
            #       chat.message_set.filter(is_readed=False).exlude(author=request.user).update(is_readed=True)
            # else:
            #       chat = None

        except:
            chat = None
        return render(request,'privatmessages/messages.html',{'user_profile':request.user,'chat':chat,'form':MessageForm()})
    def post(self,request,chat_id):
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.chat_id=chat_id
            message.author = request.user
            message.save()
        return redirect(reverse('messages', kwargs={'chat_id': chat_id}))