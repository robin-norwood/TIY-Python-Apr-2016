# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 04:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simplecontent', '0008_auto_20160519_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateField(auto_now_add=True, db_index=True),
        ),
    ]