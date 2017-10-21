# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-21 13:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171019_0806'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='discount',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='trader',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
