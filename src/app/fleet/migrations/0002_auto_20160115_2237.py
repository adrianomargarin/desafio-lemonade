# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fleet',
            name='description',
            field=models.TextField(max_length=1000, null=True, verbose_name='Descri\xe7\xe3o', blank=True),
        ),
    ]
