# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0003_fleet_is_rented'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fleet',
            options={'verbose_name': 'Frota', 'verbose_name_plural': 'Frotas'},
        ),
    ]
