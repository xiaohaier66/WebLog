# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-26 08:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mood',
        ),
        migrations.DeleteModel(
            name='Mood',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
