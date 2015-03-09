# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Banksphere', '0003_auto_20150309_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projetos',
            options={'verbose_name_plural': 'Projetos', 'verbose_name': 'Projeto', 'ordering': ['nome']},
        ),
    ]
