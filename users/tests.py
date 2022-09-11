from django.test import TestCase

# Create your tests here.
d = [3,55,344,345,400,404,443,544,577,609,709,782,799,802,803,900,901,904,915,921,925,930]


def binary_search(lists,search_num,start=0,end=0,mid=0):
    print(start,mid,end)
    if d[mid]==search_num:
        return mid
    else:
        if d[mid]>search_num:
            mid = (start+len(d))//2
            return binary_search(lists,search_num,mid,len(d),mid)
        else:
            mid=mid//2
            return binary_search(lists,search_num,start,mid,mid)

print(binary_search(d,443,0,len(d),len(d)//2))
