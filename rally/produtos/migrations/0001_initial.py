# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-16 14:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Etiqueta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=250)),
                ('descricao', models.CharField(max_length=500)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=20)),
                ('produto_logo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.AddField(
            model_name='etiqueta',
            name='Produto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produtos.Produto'),
        ),
    ]