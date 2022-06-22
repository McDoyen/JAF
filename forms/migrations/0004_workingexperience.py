# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2022-06-22 19:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0003_auto_20220622_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkingExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('title_index', models.IntegerField(default=0)),
                ('input_type', models.CharField(choices=[('text', 'text'), ('date', 'date')], default='text', max_length=6)),
            ],
        ),
    ]
