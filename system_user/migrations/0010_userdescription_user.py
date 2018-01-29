# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-03 18:21
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('system_user', '0009_auto_20180101_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdescription',
            name='user',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
