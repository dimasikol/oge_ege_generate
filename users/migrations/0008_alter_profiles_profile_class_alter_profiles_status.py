# Generated by Django 4.0.4 on 2023-01-09 11:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_profiles_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='profile_class',
            field=models.ForeignKey(blank=True, default='0', on_delete=django.db.models.deletion.CASCADE, related_name='clas_num', to='users.clas'),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='status',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 1, 9, 11, 30, 31, 381347)),
        ),
    ]
