# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-27 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipale', '0011_auto_20180127_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='Regime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sGluten', models.NullBooleanField()),
                ('sLactose', models.NullBooleanField()),
                ('vegetarien', models.NullBooleanField()),
                ('vegan', models.NullBooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='menu',
            name='regime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.Regime'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='regime',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.Regime'),
        ),
    ]
