# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-24 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipale', '0008_reservation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='pain',
        ),
        migrations.AddField(
            model_name='reservation',
            name='pain',
            field=models.NullBooleanField(),
        ),
    ]
