# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0012_remove_estudiante_estudiante_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='es_favorito',
            field=models.BooleanField(default=False),
        ),
    ]
