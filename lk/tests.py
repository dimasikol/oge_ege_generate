from django.test import TestCase

# Create your tests here.


def last_five_elemenst(lists):
    if len(lists)>5:
        return lists[-1:-6:-1]
    return lists

d=last_five_elemenst([1,5,6,8,8,22])
print(d)