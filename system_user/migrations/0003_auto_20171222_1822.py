# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-12-22 18:22
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system_user', '0002_auto_20171222_1744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdescription',
            old_name='physical_activity_id',
            new_name='physical_activity',
        ),
        migrations.RemoveField(
            model_name='usersickness',
            name='user_sickness',
        ),
        migrations.AddField(
            model_name='userdescription',
            name='sickness',
            field=models.ManyToManyField(to='system_user.UserSickness'),
        ),
        migrations.AlterField(
            model_name='userdescription',
            name='birthday',
            field=models.DateField(default=datetime.date.today, verbose_name='Birthday'),
        ),
        migrations.AlterField(
            model_name='userdescription',
            name='height',
            field=models.DecimalField(decimal_places=5, max_digits=8, verbose_name='Height in meters'),
        ),
        migrations.AlterField(
            model_name='userdescription',
            name='weight',
            field=models.DecimalField(decimal_places=5, max_digits=8, verbose_name='Weight in kilograms'),
        ),
    ]