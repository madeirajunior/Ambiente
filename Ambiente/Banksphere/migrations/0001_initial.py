# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projetos',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('ens', models.CharField(max_length=100, verbose_name='Aplicações')),
            ],
            options={
                'verbose_name_plural': 'Projetos',
                'ordering': ['nome'],
                'verbose_name': 'Projeto',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servidores',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('so', models.CharField(max_length=30, choices=[('LINUX', 'LINUX'), ('WINDOWS', 'WINDOWS'), ('AIX', 'AIX'), ('SOLARIS', 'SOLARIS')], verbose_name='Sistema Operacional')),
                ('ambiente', models.CharField(max_length=30, choices=[('PRODUÇÃO', 'PRODUÇÃO'), ('PRÉ', 'PRÉ'), ('OCULTO', 'OCULTO'), ('PROVA-INTEGRADA', 'PROVA-INTEGRADA')], verbose_name='Ambiente')),
                ('projeto', models.ForeignKey(to='Banksphere.Projetos', related_name='Projetos')),
            ],
            options={
                'verbose_name_plural': 'Servidores',
                'verbose_name': 'Servidor',
            },
            bases=(models.Model,),
        ),
    ]
