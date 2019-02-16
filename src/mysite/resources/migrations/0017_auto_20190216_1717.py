# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('resources', '0016_evaluacion_comentario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='es_favorito',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='profesor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, on_delete=django.db.models.deletion.SET_NULL),
        ),
    ]
