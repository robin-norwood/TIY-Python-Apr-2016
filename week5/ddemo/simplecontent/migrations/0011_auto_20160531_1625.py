# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 16:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simplecontent', '0010_auto_20160523_1351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'permissions': (('moderate_comment', 'Can the user moderate comments?'), ('view_unmoderated_comment', 'Can the user view unmoderated comments?'))},
        ),
        migrations.AlterModelManagers(
            name='article',
            managers=[
            ],
        ),
    ]
