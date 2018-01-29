# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-21 16:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledgebased', '0002_auto_20180116_0616'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rules',
            old_name='name',
            new_name='domain',
        ),
        migrations.RemoveField(
            model_name='rules',
            name='and_user_diet_is',
        ),
        migrations.RemoveField(
            model_name='rules',
            name='if_food_diet_is',
        ),
        migrations.AddField(
            model_name='rules',
            name='fuzzy_association_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='rules',
            name='name_of_variable',
            field=models.CharField(default='', max_length=255),
        ),
    ]
