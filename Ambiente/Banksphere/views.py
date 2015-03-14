#-*- coding:utf-8 -*-

from django.shortcuts import render
from django.views.generic import ListView
from Banksphere.models import Projetos, Servidores, AppEns, AppServers


def lista_proj(request):
    """ Lista todos os projetos. """
    proj = Projetos.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        proj = proj.filter(nome__icontains=var_get_search)
    return render(request, 'lista_projetos.html', {'proj': proj})


def proj_detail(request, pk):
    """Mostra os servidores do Projeto"""
    projeto = Projetos.objects.get(pk=pk)
    servidor = Servidores.objects.all().filter(projeto=projeto)
    
    servidor_id = Servidores.objects.get(pk=pk)
    appserv = AppServers.objects.all().filter(servidor_id=servidor_id) 
    
    context = {'servidores': servidor, 'projetos': projeto, 'appservers': appserv, 'servidor_id': servidor_id}
    return render(request, 'servidores_detail.html', context)


