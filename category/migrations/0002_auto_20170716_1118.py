# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catalogue',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='catalogue',
            new_name='Category',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='product/%Y/%m/%d', verbose_name='Image'),
        ),
    ]
