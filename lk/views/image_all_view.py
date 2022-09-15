from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from users.models import AlbomsImage

class ImagesView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request,user_name):
        image_user = AlbomsImage.objects.filter(profile_albomsimage__user__username=user_name)
        return render(request,'lk/personal_account/albom_list.html',{'albom':image_user})