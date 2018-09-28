# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_remove_estudiante_fecha_de_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion',
            name='es_favorito',
            field=models.BooleanField(default=False),
        ),
    ]
