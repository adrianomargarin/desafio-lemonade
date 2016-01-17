# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fleet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Nome')),
                ('category', models.CharField(max_length=10, verbose_name='Categoria', choices=[('motorcycle', 'Moto'), ('car', 'Carro'), ('utility', 'Utilit\xe1rio'), ('truck', 'Caminh\xe3o')])),
                ('description', models.CharField(max_length=1000, null=True, verbose_name='Descri\xe7\xe3o', blank=True)),
            ],
        ),
    ]
