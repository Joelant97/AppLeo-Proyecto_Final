# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0004_estudiante_estudiante_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='estudiante_id',
            field=models.CharField(max_length=5, default='Introdusca el ID'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='estudiante_logo',
            field=models.CharField(max_length=1000, default='LINK de la Imagen'),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='profesor_id',
            field=models.CharField(max_length=5, default='Introdusca el ID'),
        ),
    ]
