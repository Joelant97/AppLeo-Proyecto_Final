# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import phone_field.models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comprension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('comprension_porcentaje', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombres', models.CharField(max_length=250)),
                ('apellidos', models.CharField(max_length=250)),
                ('genero', models.CharField(max_length=10)),
                ('edad', models.CharField(max_length=8)),
                ('foto', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('texto_a_leer', models.CharField(max_length=500, default='María conoce un niño con muy mal carácter en su escuela llamado Juan Carlos')),
                ('evaluacion_tipo', models.CharField(max_length=15)),
                ('fluidez_lectora', models.CharField(max_length=25, default='')),
                ('tipo_lectura', models.CharField(max_length=250, default='')),
                ('es_favorito', models.BooleanField(default=False)),
                ('comentario', models.CharField(blank=True, max_length=100)),
                ('fecha', models.DateTimeField(default=datetime.datetime.now)),
                ('estudiante', models.ForeignKey(to='resources.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='Fluidez',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('ppm', models.CharField(max_length=8)),
                ('tipo_lectura', models.CharField(max_length=250)),
                ('evaluacion', models.ForeignKey(to='resources.Evaluacion')),
            ],
        ),
        migrations.CreateModel(
            name='Lectura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('titulo', models.CharField(max_length=250)),
                ('texto', models.CharField(max_length=1500)),
            ],
        ),
        migrations.CreateModel(
            name='Pregunta',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('nombre_p1', models.CharField(blank=True, max_length=150)),
                ('enunciado_p1', models.CharField(blank=True, max_length=512)),
                ('nombre_p2', models.CharField(blank=True, max_length=150)),
                ('enunciado_p2', models.CharField(blank=True, max_length=512)),
                ('nombre_p3', models.CharField(blank=True, max_length=150)),
                ('enunciado_p3', models.CharField(blank=True, max_length=512)),
                ('nombre_p4', models.CharField(blank=True, max_length=150)),
                ('enunciado_p4', models.CharField(blank=True, max_length=512)),
                ('nombre_p5', models.CharField(blank=True, max_length=150)),
                ('enunciado_p5', models.CharField(blank=True, max_length=512)),
                ('lectura', models.ForeignKey(to='resources.Lectura', default='', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('direccion', models.CharField(blank=True, max_length=250)),
                ('telefono', phone_field.models.PhoneField(blank=True, max_length=31, help_text='Teléfono de contacto')),
                ('usuario', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='evaluacion',
            name='lectura',
            field=models.ForeignKey(to='resources.Lectura', default='', blank=True),
        ),
        migrations.AddField(
            model_name='comprension',
            name='evaluacion',
            field=models.ForeignKey(to='resources.Evaluacion'),
        ),
    ]
