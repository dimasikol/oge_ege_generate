from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User

class NewsCategoryModel(models.Model):
    name = models.CharField(max_length=55,unique=True)
    slug = models.SlugField(max_length=70,unique=True)
    preview = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to='media/news/news_category/',blank=True)

class PostNewsCategoryModel(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    image = models.ImageField(upload_to=f'media/news/posts/',blank=True)
    text = RichTextUploadingField()
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(NewsCategoryModel,on_delete=models.CASCADE,related_name='category_news')
    author = models.ManyToManyField(User,related_name='post_author')
