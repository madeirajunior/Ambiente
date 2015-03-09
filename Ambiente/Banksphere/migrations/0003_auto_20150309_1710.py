# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Banksphere', '0002_auto_20150309_1707'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='projetos',
            options={'verbose_name_plural': 'Projetos', 'verbose_name': 'Projeto'},
        ),
        migrations.AlterModelOptions(
            name='servidores',
            options={'verbose_name_plural': 'Servidores', 'verbose_name': 'Servidor'},
        ),
    ]
