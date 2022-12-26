from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import NewsCategoryModel,PostNewsCategoryModel


class NewsView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get(self,request):
        if request.method =='GET':
            self.category=NewsCategoryModel.objects.all()
            self.context = {'context': self.category}
            return render(request,template_name='news/temp/news_list.html',context=self.context)

class  PostListView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    def get(self,request,category_post):
        if request.method=='GET':
            self.post = PostNewsCategoryModel.objects.filter(category__slug=category_post)
            self.context = {'context': self.post}
            return render(request, template_name='news/temp/post_list.html', context=self.context)

class PostDetailView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly,]
    def get(self,request,**kwargs):

        self.post = PostNewsCategoryModel.objects.get(slug=kwargs['post_slug'])
        self.context = {'context':self.post}
        return render(request,template_name='news/temp/post_detail.html',context=self.context)


