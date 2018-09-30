# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('resources', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comprension',
            name='comprension_porcentaje',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='edad',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='fluidez',
            name='ppm',
            field=models.CharField(max_length=8),
        ),
    ]
