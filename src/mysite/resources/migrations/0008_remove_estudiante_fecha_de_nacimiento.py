# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('resources', '0007_auto_20180928_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='fecha_de_nacimiento',
        ),
    ]
