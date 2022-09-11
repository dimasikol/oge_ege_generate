import datetime

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django import forms



class Profiles(models.Model):
    DATA={
        'zodiac':(('',""),('Овен','Овен'), ('Телец','Телец'), ('Близнецы','Близнецы'), ('Рак','Рак'), ('Лев','Лев'), ('Дева','Дева'), ('Весы','Весы'), ('Скорпион','Скорпион'), ('Стрелец','Стрелец'), ('Козерог','Козерог'), ('Водолей','Водолей'), ('Рыбы','Рыбы')),
        'socionics_type':(('',''), ('Дюма','Дюма'), ('Гюго','Гюго'), ('Робеспьер','Робеспьер'), ('Гамлет','Гамлет'), ('Максим Горький','Максим Горький'),('Жуков','Жуков'),('Есенин','Есенин'),('Наполеон','Наполеон'),('Бальзак','Бальзак'),('Джек Лондон','Джек Лондон'),('Драйзер','Драйзер'),('Штирлиц','Штирлиц'),('Достоевский','Достоевский'),('Гексли','Гексли'),('Габен','Габен'),('Дон Кихот','Дон Кихот'))
          }
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profiles')
    image_profile = models.ImageField(verbose_name='фото профиля',upload_to=f"media/lk/%Y/%m/%d/",blank=True,default='media/bShop/temp/shablon.jpg')
    location = models.CharField(verbose_name='место раположения',max_length=40,blank=True,default='ru')
    about = models.TextField(blank=True)
    birthday = models.DateField(default=datetime.date.today)
    city = models.CharField(max_length=15,blank=True,default='')
    zodiac = models.CharField(max_length=25,choices=DATA['zodiac'], default='',blank=True)
    socionics_type = models.CharField(max_length=25,choices=DATA['socionics_type'],default='',blank=True)
    def __str__(self):
        return  f'{self.id} {self.user}'

class Clas(models.Model):
    clas = models.CharField(max_length=4,blank=True)
    profile_class = models.ForeignKey(Profiles,on_delete=models.DO_NOTHING,related_name='clas')


class Education(models.Model):
    education_type = models.CharField(max_length=45,blank=True)
    profile_education = models.ForeignKey(Profiles,on_delete=models.DO_NOTHING,related_name='education')


class AlbomsImage(models.Model):
    image = models.ImageField(upload_to='media/user/albomimage/%Y/%m/%d/',blank=True)
    profile_albomsimage = models.ForeignKey(Profiles,on_delete=models.DO_NOTHING,related_name='albom')
    class Meta:
        ordering = ['-id',]


class Friendship(models.Model):
    user_name = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name='friend_user')
    profile_friendshiop = models.ForeignKey(Profiles,on_delete=models.DO_NOTHING,related_name='freanship')
