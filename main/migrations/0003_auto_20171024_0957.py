# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 09:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_videos_youtubevid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(editable=False, max_length=100, unique=True)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Subjects')),
            ],
        ),
        migrations.AlterField(
            model_name='videos',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Chapters'),
        ),
    ]
