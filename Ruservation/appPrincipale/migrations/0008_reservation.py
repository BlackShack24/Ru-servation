# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-22 21:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipale', '0007_auto_20171222_2252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.FloatField()),
                ('date', models.DateTimeField()),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.Menu')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.UserProfile')),
            ],
        ),
    ]
