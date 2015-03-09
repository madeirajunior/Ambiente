#-*- coding: utf-8 -*-
from django.db import models
from random import choice

# Create your models here.

class Projetos(models.Model):
    nome = models.CharField("Nome", max_length=100)
    
    def __str__(self):
            return self.nome
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'

class Servidores(models.Model):
    nome = models.CharField("Nome", max_length=100)
    projeto = models.ForeignKey("Projetos", related_name="Projetos")
    so = models.CharField("Sistema Operacional", choices=(
        ('LINUX', "LINUX"),
        ('WINDOWS', "WINDOWS"),
        ('AIX', "AIX"),
        ('SOLARIS', "SOLARIS"),   
    ),
        max_length=30
    )
    
    ambiente = models.CharField("Ambiente", choices=(
        ('PRODUÇÃO', "PRODUÇÃO"),
        ('PRÉ', "PRÉ"),
        ('OCULTO', "OCULTO"),
        ('PROVA-INTEGRADA', "PROVA-INTEGRADA"),    
    ),
        max_length=30
    )
    
    class Meta:
        #ordering = ['nome']
        verbose_name = 'Servidor'
        verbose_name_plural = 'Servidores'

    def __str__(self):
        return self.nome