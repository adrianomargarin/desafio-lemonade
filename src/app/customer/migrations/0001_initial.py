# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields
from django.conf import settings
import app.core.validators
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cpf', models.CharField(unique=True, max_length=11, verbose_name='CPF', validators=[app.core.validators.validate_cpf])),
                ('cnh_type', multiselectfield.db.fields.MultiSelectField(max_length=9, verbose_name='Tipo da CNH', choices=[('A', 'Categoria A'), ('B', 'Categoria B'), ('C', 'Categoria C'), ('D', 'Categoria D'), ('E', 'Categoria E')])),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
