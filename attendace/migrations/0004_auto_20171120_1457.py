# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendace', '0003_delete_attendancerecord'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='status',
        ),
        migrations.AddField(
            model_name='department',
            name='Department',
            field=models.CharField(blank=True, choices=[('c', 'CITE '), ('a', 'CBA '), ('b', 'ASCEND ')], default='m', help_text='Department', max_length=1),
        ),
    ]
