from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from users.models import Profiles

class ImagesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,user_name):
        image_user = Profiles.objects.filter(user_id__username=user_name)
        print(image_user)
        return render(request,'lk/personal_account/albom_list.html',{'albom':image_user})