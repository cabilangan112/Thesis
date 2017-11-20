# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 08:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendace', '0009_auto_20171120_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='Department',
            field=models.CharField(blank=True, choices=[('CITE', 'College of information and Technology  '), ('CBA', 'College Busnisss And Accountancy'), ('ASCEND', 'ASCEND ')], default='b', help_text='Department', max_length=8),
        ),
        migrations.AlterField(
            model_name='student',
            name='Sex',
            field=models.CharField(blank=True, choices=[('m', 'Male'), ('F', 'Female')], default='m', max_length=1),
        ),
    ]
