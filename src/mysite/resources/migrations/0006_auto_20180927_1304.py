# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0005_auto_20180927_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='estudiante_id',
            field=models.CharField(max_length=5, default='Introduzca el ID'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='profesor_id',
            field=models.CharField(max_length=5, default='Introduzca el ID'),
        ),
    ]
