# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-25 14:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_ref', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='ushou',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='uemail',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='upwd',
            field=models.CharField(max_length=40),
        ),
    ]
