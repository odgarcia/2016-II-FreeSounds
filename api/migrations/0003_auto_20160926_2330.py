# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-27 04:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20160926_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='piece',
            old_name='imageCover',
            new_name='image_cover',
        ),
    ]