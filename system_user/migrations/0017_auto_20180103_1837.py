# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-03 18:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('system_user', '0016_auto_20180103_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdescription',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
