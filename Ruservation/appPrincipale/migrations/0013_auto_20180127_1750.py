# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-27 16:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipale', '0012_auto_20180127_1745'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allergie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sGluten', models.NullBooleanField()),
                ('sLactose', models.NullBooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='regime',
            name='sGluten',
        ),
        migrations.RemoveField(
            model_name='regime',
            name='sLactose',
        ),
        migrations.AddField(
            model_name='menu',
            name='allergie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.Allergie'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='allergie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.Allergie'),
        ),
    ]
