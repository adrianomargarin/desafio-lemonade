# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentacar', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rentacar',
            options={'verbose_name': 'Aluguel', 'verbose_name_plural': 'Alugu\xe9is'},
        ),
        migrations.AddField(
            model_name='rentacar',
            name='is_back',
            field=models.BooleanField(default=False, verbose_name=b'J\xc3\xa1 foi devolvido?'),
        ),
    ]
