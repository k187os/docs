# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-07 23:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0003_auto_20170518_0003'),
    ]

    operations = [
        migrations.RenameField(
            model_name='drug',
            old_name='drug_famille',
            new_name='drug_dci',
        ),
        migrations.AddField(
            model_name='drug',
            name='drug_cnas',
            field=models.IntegerField(max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='drug',
            name='drug_obs',
            field=models.CharField(max_length=100, null=True),
        ),
    ]