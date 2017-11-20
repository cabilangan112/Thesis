# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 07:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendace', '0004_auto_20171120_1457'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='Department',
            field=models.CharField(blank=True, choices=[('c', 'CITE  '), ('a', 'CBA '), ('b', 'ASCEND ')], default='c', help_text='Department', max_length=1),
        ),
    ]