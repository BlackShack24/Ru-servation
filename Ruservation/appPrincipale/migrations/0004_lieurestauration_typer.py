# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-19 13:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipale', '0003_auto_20171219_1417'),
    ]

    operations = [
        migrations.AddField(
            model_name='lieurestauration',
            name='typeR',
            field=models.CharField(choices=[('RU', 'Restaurant Universitaire'), ('BR', 'Brasserie'), ('CA', 'Cafétéria'), ('FO', 'Foodtruck'), ('SA', 'Salle administrative'), ('SW', 'Sandwicherie')], max_length=2, null=True),
        ),
    ]
