# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendace', '0008_auto_20171120_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Sex',
            field=models.CharField(blank=True, choices=[('m', 'Male'), ('F', 'Female')], default='m', max_length=5),
        ),
    ]
