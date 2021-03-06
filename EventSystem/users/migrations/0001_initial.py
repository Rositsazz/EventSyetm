# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-18 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseUser',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True,
                                        serialize=False,
                                        verbose_name='ID')),
                ('password', models.CharField(max_length=128,
                                              verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True,
                                                    null=True,
                                                    verbose_name='last login')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True,
                                                    null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
