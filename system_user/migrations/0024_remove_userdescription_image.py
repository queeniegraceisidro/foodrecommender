# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-16 05:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('system_user', '0023_remove_userdescription_birthday'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdescription',
            name='image',
        ),
    ]
