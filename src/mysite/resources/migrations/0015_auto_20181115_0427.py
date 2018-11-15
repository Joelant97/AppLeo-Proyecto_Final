# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0014_evaluacionform'),
    ]

    operations = [
        migrations.DeleteModel(
            name='EvaluacionForm',
        ),
        migrations.RemoveField(
            model_name='evaluacion',
            name='evaluacion_id',
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='fluidez_lectora',
            field=models.CharField(max_length=25, default=''),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='texto_a_leer',
            field=models.CharField(max_length=500, default='María conoce un niño con muy mal carácter en su escuela llamado Juan Carlos'),
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='tipo_lectura',
            field=models.CharField(max_length=250, default=''),
        ),
    ]
