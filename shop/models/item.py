from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.urls import reverse
from .subcategory import  SubCategory
from .model import Model


class Items(models.Model):
    keyitem = models.CharField(verbose_name='Код товара', max_length=1000, blank=True, default='0')
    name = models.CharField(verbose_name='Наименование товара', max_length=250)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    description = RichTextUploadingField()
    price = models.IntegerField(verbose_name='Цена', blank=True, default=100)
    #price_with_skidka = models.
    skidka = models.BooleanField(verbose_name='Скида', default=False, blank=True)
    #skidka_procent = models.
    count = models.IntegerField(verbose_name='Кол=во', default=0, blank=True)
    url = models.SlugField(max_length=266)
    image = models.ImageField(verbose_name='Главное фото', upload_to='media/bShop/Item/%Y/%m/%d/')
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not (self.url):
            self.url = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('items', kwargs=self.kwargs['url'])

    class Meta:
        db_table = 'bShop_item'


class ReviewsItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    item = models.ForeignKey(Items, on_delete=models.SET_NULL, null=True)


    class Meta:
        db_table = 'bShop_reviewsitem'

class ImageItems(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(verbose_name='Главное фото', upload_to='media/bShop/Item/%Y/%m/%d/')
    item = models.ForeignKey(Items, on_delete=models.SET_NULL, null=True)


    class Meta:
        db_table = 'bShop_imageitems'
