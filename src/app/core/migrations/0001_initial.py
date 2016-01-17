# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import migrations, models
from django.contrib.auth.models import User

def create_superuser(apps, schema_editor):

    user = User.objects.create_superuser(username="admin",
        email="email@email.com", password="admin")

class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.RunPython(create_superuser),
    ]
