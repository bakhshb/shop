# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-16 16:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogues', '0003_auto_20170616_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]