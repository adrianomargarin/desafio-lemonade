# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0002_auto_20160115_2237'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RentACar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mileage_rotated', models.DecimalField(null=True, verbose_name='Quilometragem rodada', max_digits=7, decimal_places=2, blank=True)),
                ('customer', models.ForeignKey(verbose_name='Cliente', to='customer.Customer')),
                ('vehicle', models.ForeignKey(verbose_name='Ve\xedculo', to='fleet.Fleet')),
            ],
        ),
    ]
