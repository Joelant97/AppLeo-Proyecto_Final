# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0013_estudiante_es_favorito'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvaluacionForm',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('texto_a_leer', models.CharField(max_length=500, default='María conoce un niño con muy mal carácter en su escuela')),
            ],
        ),
    ]
