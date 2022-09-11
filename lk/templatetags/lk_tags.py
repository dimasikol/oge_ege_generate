from django import template

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

