# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0015_auto_20181115_0427'),
    ]

    operations = [
        migrations.AddField(
            model_name='evaluacion',
            name='comentario',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
