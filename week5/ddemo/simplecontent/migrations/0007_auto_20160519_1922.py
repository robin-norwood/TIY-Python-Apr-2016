# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 19:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simplecontent', '0006_auto_20160519_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='superheropower',
            name='hero',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='simplecontent.SuperHero'),
        ),
    ]
