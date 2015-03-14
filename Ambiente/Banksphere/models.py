
from django.db import models


class Projetos(models.Model):
    nome = models.CharField("Nome", max_length=100)
    
    
    def __str__(self):
            return self.nome
    
    def get_servidores_count(self):
        return self.projeto.count()
    
    def get_proj_detail_url(self):
        return u"/proj_detail/%i" % self.id
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'projeto'
        verbose_name_plural = 'projetos'

class Servidores(models.Model):
    nome = models.CharField("Nome", max_length=100)
    projeto = models.ForeignKey("Projetos", related_name="projeto")  
    so = models.CharField("Sistema Operacional", choices=(
        ('Linux', "Linux"),
        ('Windows', "Windows"),
        ('Aix', "Aix"),
        ('Solaris', "Solaris"),   
    ),
        max_length=30
    )
    
    ambiente = models.CharField("Ambiente", choices=(
        ('Produção', "Produção"),
        ('Pré', "Pré"),
        ('Oculto', "Oculto"),
        ('Prova Integrada', "Prova Integrada"),    
    ),
        max_length=30
    )
    
    funcao = models.CharField("Função", choices=(
        ('DMGR', "Dmgr"),
        ('WEBSPHERE', "Was"),
        ('IHS-WEB', "Ihs-Web"),
        ('DB2', "Db2"),    
    ),
        max_length=30
    )
    
    ip = models.IPAddressField("Endereço IP", max_length=30)
    celula = models.CharField("Celula", max_length=30)
       
    class Meta:
        ordering = ['nome']
        verbose_name = 'servidor'
        verbose_name_plural = 'servidores'

    def __str__(self):
        return self.nome
    
class AppServers(models.Model):
    nome = models.CharField("Nome", max_length=100)
    servidor = models.ForeignKey("Servidores", related_name="serv" )
    cluster = models.CharField("cluster", max_length =30)
        
    class Meta:
        ordering = ['nome']
        verbose_name = 'appserver'
        verbose_name_plural = 'appservers'
    
    def __str__(self):
        return self.nome

class AppEns(models.Model):
    nome_ens = models.CharField("Nome", max_length=100)
    arch_ens = models.CharField("Arquitetura", max_length = 50)
    cluster_ens = models.ForeignKey("AppServers", related_name="cluster_ens")
            
    class Meta:
        ordering = ['nome_ens']
        verbose_name = 'appens'
        verbose_name_plural = 'appens'
    
    def __str__(self):
        return self.nome