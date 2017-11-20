# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 08:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendace', '0006_auto_20171120_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='Department',
            field=models.CharField(blank=True, choices=[('c', 'CITE  '), ('a', 'CBA '), ('b', 'ASCEND ')], default='b', help_text='Department', max_length=1),
        ),
    ]