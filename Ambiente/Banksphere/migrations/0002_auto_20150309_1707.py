# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Banksphere', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetos',
            name='nome',
            field=models.CharField(verbose_name='Nome', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servidores',
            name='ambiente',
            field=models.CharField(verbose_name='Ambiente', max_length=30, choices=[('PRODUÇÃO', 'PRODUÇÃO'), ('PRÉ', 'PRÉ'), ('OCULTO', 'OCULTO'), ('PROVA-INTEGRADA', 'PROVA-INTEGRADA')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servidores',
            name='nome',
            field=models.CharField(verbose_name='Nome', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='servidores',
            name='so',
            field=models.CharField(verbose_name='Sistema Operacional', max_length=30, choices=[('LINUX', 'LINUX'), ('WINDOWS', 'WINDOWS'), ('AIX', 'AIX'), ('SOLARIS', 'SOLARIS')]),
            preserve_default=True,
        ),
    ]
