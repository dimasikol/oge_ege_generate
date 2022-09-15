# Generated by Django 4.0.4 on 2022-07-23 01:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_albomsimage_image_alter_clas_clas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profiles',
            name='albomimage',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='clas',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='education',
        ),
        migrations.RemoveField(
            model_name='profiles',
            name='frienship',
        ),
        migrations.AddField(
            model_name='albomsimage',
            name='profile_albomsimage',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='users.profiles'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clas',
            name='profile_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='users.profiles'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='education',
            name='profile_education',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='users.profiles'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friendship',
            name='profile_friendshiop',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='users.profiles'),
            preserve_default=False,
        ),
    ]