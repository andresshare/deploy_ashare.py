# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-29 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('telefono', models.CharField(max_length=15)),
                ('mensaje', models.CharField(max_length=300)),
            ],
        ),
    ]
