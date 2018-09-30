# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('resources', '0002_auto_20180916_2338'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='estudiante_id',
            field=models.CharField(default='SOME STRING', max_length=5),
        ),
        migrations.AddField(
            model_name='profesor',
            name='profesor_id',
            field=models.CharField(default='SOME STRING', max_length=5),
        ),
    ]
