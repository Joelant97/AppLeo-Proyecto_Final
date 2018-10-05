# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0011_auto_20181002_1815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='estudiante_id',
        ),
    ]
