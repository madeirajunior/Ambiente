
from django.db import models


class Projetos(models.Model):
    nome = models.CharField("Nome", max_length=100)
    
    def get_servidores_count(self):
        return self.servidores.count()
    
    def get_proj_detail_url(self):
        return u"/proj/%i" % self.id
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'projeto'
        verbose_name_plural = 'projetos'
    
    def __str__(self):
        return self.nome

class Servidores(models.Model):
    nome = models.CharField("Nome", max_length=100)
    projeto = models.ForeignKey("Projetos", related_name="servidores")
    
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
    
    def get_serv_id(self):
        return u"%i" % self.id
        
    def get_serv_appsrv(self):
        return self.appservers.count()
    
    def __str__(self):
        return u"%s" %self.nome
    class Meta:
        ordering = ['nome']
        verbose_name = 'servidor'
        verbose_name_plural = 'servidores'
    
        
class AppServers(models.Model):
    nome = models.CharField("Nome", max_length=100)
    cluster = models.CharField("Cluster", max_length=100)
    servidor = models.ForeignKey("Servidores", related_name="appservers")
    projeto = models.ForeignKey("Projetos", related_name="projetos")
    
    def get_appserv_detail_nome(self):
        return u"%s" % self.nome
            
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['nome']
        verbose_name = 'appserver'
        verbose_name_plural = 'appservers'
    
