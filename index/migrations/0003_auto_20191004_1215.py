# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-10-04 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20191004_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]