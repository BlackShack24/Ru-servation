# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-27 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipale', '0010_auto_20171224_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favoris',
            name='lieu',
        ),
        migrations.AddField(
            model_name='favoris',
            name='lieu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.LieuRestauration'),
        ),
    ]