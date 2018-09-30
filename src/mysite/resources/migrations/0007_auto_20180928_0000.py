# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('resources', '0006_auto_20180927_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='estudiante_apellido',
            new_name='apellidos',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='nacimiento',
            new_name='fecha_de_nacimiento',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='estudiante_genero',
            new_name='genero',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='estudiante_nombre',
            new_name='nombres',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='estudiante_logo',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='foto',
            field=models.CharField(max_length=1000, default='LINK de la FOTO'),
        ),
    ]
