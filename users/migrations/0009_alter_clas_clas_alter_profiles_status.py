# Generated by Django 4.0.4 on 2023-01-09 11:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_alter_profiles_profile_class_alter_profiles_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clas',
            name='clas',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='status',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 9, 11, 44, 54, 760148)),
        ),
    ]
