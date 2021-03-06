# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-22 21:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appPrincipale', '0006_favoris'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuBoisson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boisson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.Boisson')),
            ],
        ),
        migrations.CreateModel(
            name='MenuDessert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dessert', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.Dessert')),
            ],
        ),
        migrations.CreateModel(
            name='MenuEntree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entree', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.Entree')),
            ],
        ),
        migrations.CreateModel(
            name='MenuFromage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fromage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.Fromage')),
            ],
        ),
        migrations.CreateModel(
            name='MenuPlatPrincipal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='menu',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='lieurestauration',
            name='boisson',
        ),
        migrations.RemoveField(
            model_name='lieurestauration',
            name='dessert',
        ),
        migrations.RemoveField(
            model_name='lieurestauration',
            name='entree',
        ),
        migrations.RemoveField(
            model_name='lieurestauration',
            name='fromage',
        ),
        migrations.RemoveField(
            model_name='lieurestauration',
            name='platPrincipal',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='prix',
        ),
        migrations.AddField(
            model_name='menu',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.RemoveField(
            model_name='menu',
            name='boisson',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='dessert',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='entree',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='fromage',
        ),
        migrations.RemoveField(
            model_name='menu',
            name='platPrincipal',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.AddField(
            model_name='menuplatprincipal',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.Menu'),
        ),
        migrations.AddField(
            model_name='menuplatprincipal',
            name='platPrincipal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.PlatPrincipal'),
        ),
        migrations.AddField(
            model_name='menufromage',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.Menu'),
        ),
        migrations.AddField(
            model_name='menuentree',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.Menu'),
        ),
        migrations.AddField(
            model_name='menudessert',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.Menu'),
        ),
        migrations.AddField(
            model_name='menuboisson',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appPrincipale.Menu'),
        ),
        migrations.AddField(
            model_name='menu',
            name='boisson',
            field=models.ManyToManyField(through='appPrincipale.MenuBoisson', to='appPrincipale.Boisson'),
        ),
        migrations.AddField(
            model_name='menu',
            name='dessert',
            field=models.ManyToManyField(through='appPrincipale.MenuDessert', to='appPrincipale.Dessert'),
        ),
        migrations.AddField(
            model_name='menu',
            name='entree',
            field=models.ManyToManyField(through='appPrincipale.MenuEntree', to='appPrincipale.Entree'),
        ),
        migrations.AddField(
            model_name='menu',
            name='fromage',
            field=models.ManyToManyField(through='appPrincipale.MenuFromage', to='appPrincipale.Fromage'),
        ),
        migrations.AddField(
            model_name='menu',
            name='platPrincipal',
            field=models.ManyToManyField(through='appPrincipale.MenuPlatPrincipal', to='appPrincipale.PlatPrincipal'),
        ),
    ]
