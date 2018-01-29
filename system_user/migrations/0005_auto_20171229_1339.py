# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-29 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_user', '0004_userdescription_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdescription',
            name='username',
        ),
        migrations.AddField(
            model_name='userdescription',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
    ]