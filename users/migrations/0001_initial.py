# Generated by Django 4.0.4 on 2022-07-23 00:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbomsImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/user/albomimage/%Y/%m/%d/')),
            ],
        ),
        migrations.CreateModel(
            name='Clas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clas', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_type', models.CharField(blank=True, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Profiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_profile', models.ImageField(blank=True, default='media/bShop/temp/shablon.jpg', upload_to='media/lk/%Y/%m/%d/', verbose_name='фото профиля')),
                ('location', models.CharField(blank=True, default='ru', max_length=40, verbose_name='место раположения')),
                ('about', models.TextField(blank=True)),
                ('birthday', models.DateField(blank=True)),
                ('city', models.CharField(blank=True, max_length=15)),
                ('albomimage', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.albomsimage')),
                ('clas', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='users.clas')),
                ('education', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.education')),
                ('frienship', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, to='users.friendship')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]