
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.urls import reverse


class Model(models.Model):
    name = models.CharField(verbose_name='Производитель', max_length=200)
    contry = models.CharField(verbose_name='Страна', max_length=1000)

    def __str__(self):
        return self.name
