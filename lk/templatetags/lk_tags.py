from django import template
from django.contrib.auth.models import User

from users.models import Friendship
register = template.Library()

@register.filter(name='get_pos')
def get_pos(lists,id=0):
    if lists[0]=="":
        return 'вы не дали ответ'
    else:
        return lists[id]

@register.filter(name='str_to_list')
def str_to_list(strs:list,id=0):
    strs=strs[1:-1].split(',')
    return strs[int(id)]


@register.simple_tag()
def follower_count(user:str):
    if str(user).isdigit():
        return Friendship.objects.filter(user_name_id=user).count()
    return Friendship.objects.filter(user_name__username=user).count()

@register.simple_tag()
def following_count(user:str):
    if str(user).isdigit():
        return Friendship.objects.filter(profile_friendshiop=user).count()
    return Friendship.objects.filter(profile_friendshiop__user__username=user).count()


@register.simple_tag()
def messages_unread_cout():
    print()