# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-11 00:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0007_presciption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drug',
            old_name='drug_name',
            new_name='drug_nom',
        ),
    ]
