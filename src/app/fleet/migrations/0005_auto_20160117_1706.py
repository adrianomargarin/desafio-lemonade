# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0004_auto_20160116_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fleet',
            old_name='name',
            new_name='vehicle_name',
        ),
    ]
