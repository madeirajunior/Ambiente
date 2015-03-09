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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'Nome')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Projeto',
                'verbose_name_plural': 'Projetos',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Servidores',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100, verbose_name=b'Nome')),
                ('so', models.CharField(max_length=30, verbose_name=b'Sistema Operacional', choices=[(b'LINUX', b'LINUX'), (b'WINDOWS', b'WINDOWS'), (b'AIX', b'AIX'), (b'SOLARIS', b'SOLARIS')])),
                ('ambiente', models.CharField(max_length=30, verbose_name=b'Ambiente', choices=[(b'PRODU\xc3\x87\xc3\x83O', b'PRODU\xc3\x87\xc3\x83O'), (b'PR\xc3\x89', b'PR\xc3\x89'), (b'OCULTO', b'OCULTO'), (b'PROVA-INTEGRADA', b'PROVA-INTEGRADA')])),
                ('projeto', models.ForeignKey(related_name='Projetos', to='Banksphere.Projetos')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Servidor',
                'verbose_name_plural': 'Servidores',
            },
            bases=(models.Model,),
        ),
    ]
