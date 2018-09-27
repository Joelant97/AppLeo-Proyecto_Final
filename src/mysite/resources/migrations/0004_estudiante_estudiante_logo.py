# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0003_auto_20180926_1809'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='estudiante_logo',
            field=models.CharField(default='SOME STRING', max_length=1000),
        ),
    ]
