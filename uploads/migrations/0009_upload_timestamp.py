# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-15 04:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0008_auto_20170831_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='upload',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]