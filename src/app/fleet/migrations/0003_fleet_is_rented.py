# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0002_auto_20160115_2237'),
    ]

    operations = [
        migrations.AddField(
            model_name='fleet',
            name='is_rented',
            field=models.BooleanField(default=False, verbose_name='Est\xe1 alugado?'),
        ),
    ]
