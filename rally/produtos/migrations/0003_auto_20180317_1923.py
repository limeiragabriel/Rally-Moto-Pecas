# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-17 22:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0002_auto_20180316_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='produto_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
