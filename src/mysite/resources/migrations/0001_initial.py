# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comprension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('comprension_porcentaje', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('estudiante_nombre', models.CharField(max_length=250)),
                ('estudiante_apellido', models.CharField(max_length=250)),
                ('estudiante_genero', models.CharField(max_length=10)),
                ('nacimiento', models.DateField(max_length=10)),
                ('edad', models.IntegerField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('evaluacion_id', models.CharField(max_length=5)),
                ('evaluacion_tipo', models.CharField(max_length=15)),
                ('estudiante', models.ForeignKey(to='resources.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Fluidez',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ppm', models.IntegerField(max_length=4)),
                ('tipo_lectura', models.CharField(max_length=250)),
                ('evaluacion', models.ForeignKey(to='resources.Evaluacion')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('profesor_nombre', models.CharField(max_length=250)),
                ('profesor_apellido', models.CharField(max_length=250)),
                ('profesor_email', models.EmailField(max_length=250)),
                ('profesor_telefono', models.CharField(max_length=15)),
                ('profesor_genero', models.CharField(max_length=10)),
                ('institucion', models.CharField(max_length=250)),
            ],
        ),
        migrations.AddField(
            model_name='estudiante',
            name='profesor',
            field=models.ForeignKey(to='resources.Profesor'),
        ),
        migrations.AddField(
            model_name='comprension',
            name='evaluacion',
            field=models.ForeignKey(to='resources.Evaluacion'),
        ),
    ]
