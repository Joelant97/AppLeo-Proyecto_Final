# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0010_auto_20180929_2152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='profesor',
        ),
        migrations.DeleteModel(
            name='Profesor',
        ),
    ]
