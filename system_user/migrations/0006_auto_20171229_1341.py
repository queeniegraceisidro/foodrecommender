# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-29 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_user', '0005_auto_20171229_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdescription',
            name='email',
            field=models.EmailField(max_length=255),
        ),
    ]