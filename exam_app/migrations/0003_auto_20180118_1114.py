# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-18 11:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_app', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productversion',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
