# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('date', models.DateTimeField()),
                ('Diag', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('drug_name', models.CharField(max_length=100)),
                ('drug_famille', models.CharField(max_length=100)),
                ('drug_forme', models.CharField(max_length=100)),
                ('drug_dose', models.CharField(max_length=100)),
                ('drug_obs', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('Nom', models.CharField(max_length=100)),
                ('Prenom', models.CharField(max_length=100)),
                ('Gendre', models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')], default='M')),
                ('Date_Naissance', models.DateField()),
                ('Adresse', models.CharField(max_length=100, blank=True)),
                ('Mobile', models.CharField(max_length=10, blank=True)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('Sécurité_sociale', models.CharField(max_length=10, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='consultation',
            name='num',
            field=models.ForeignKey(to='clinic.Patient'),
        ),
    ]
