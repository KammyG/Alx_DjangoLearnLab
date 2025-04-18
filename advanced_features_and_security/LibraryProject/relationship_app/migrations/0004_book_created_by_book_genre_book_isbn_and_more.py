# Generated by Django 5.1.6 on 2025-02-23 15:20

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0003_userprofile'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.CharField(default='1998-09-18', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.CharField(default='1998-09-18', max_length=13, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='published_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
