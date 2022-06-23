from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify
from django.urls import reverse
from .category import Category


class SubCategory(models.Model):
    name = models.CharField(verbose_name='Подкатегория', max_length=1000)
    description = RichTextUploadingField(verbose_name='Описание')
    image = models.ImageField(verbose_name='Изображение', upload_to='media/bShop/%Y/%m/%d/', blank=True,
                              default='media/bShop/temp/shablon.jpg')
    slug = models.SlugField(verbose_name='Ссылка', max_length=1200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, default=True)

    def __str__(self):
        return self.slug

    # def save(self, *args, **kwargs):
    #     if not (self.url):

    #         self.url = slugify(self.name)
    #     super().save(*args, **kwargs)
    #
    # def get_absolute_url(self):
    #     return reverse('subcategory', kwargs=self.kwargs['url'])

    class Meta:
        db_table = 'bShop_subcategory'