# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-30 07:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_user', '0007_auto_20171230_0426'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdescription',
            name='sickness',
            field=models.ManyToManyField(blank=True, to='system_user.UserSickness'),
        ),
    ]
