# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-07 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0004_auto_20170608_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drug',
            name='drug_cnas',
            field=models.CharField(max_length=5, null=True),
        ),
    ]