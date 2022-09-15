from rest_framework.views import APIView
from rest_framework import permissions
from django.shortcuts import render
from users.models import Friendship
from django.contrib.auth.models import User
class FollowerFriendshipView(APIView):
    """вьюха в личных кабинетак пользователей/ для показа всех друзей"""
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request,user_name):
            friendships = Friendship.objects.filter(user_name_id=User.objects.get(username=user_name))
            return render(request,'lk/personal_account/friends_list.html',{'friendship':friendships,'user_name':user_name})


class FolowingFriendshipView(APIView):
    permission_classes=[permissions.IsAuthenticated]
    def get(self,request,user_name:str):
        if user_name.isdigit():
            friendships = Friendship.objects.filter(profile_friendshiop=user_name)
        else:
            friendships = Friendship.objects.filter(profile_friendshiop__user__username=user_name)
        return render(request, 'lk/personal_account/following_list.html', {'friendship': friendships, 'user_name': user_name})
