#-*- coding:utf-8 -*-

from django.shortcuts import render

from Banksphere.models import Projetos, Servidores, AppServers


def lista_proj(request):
    """ Lista todos os projetos. """
    proj = Projetos.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is not None:
        proj = proj.filter(nome__icontains=var_get_search)
    return render(request, 'lista_projetos.html', {'proj': proj})


def proj(request, pk):
   
    projeto = Projetos.objects.get(pk=pk)
    servidor = Servidores.objects.all().filter(projeto=projeto)
    context = {'servidores': servidor, 'projetos': projeto}
    return render(request, 'servidores_detail.html', context)

"""
def proj(request, pk, id):
   
    projeto = Projetos.objects.get(pk=pk)
    servidor = Servidores.objects.all().filter(projeto=projeto)
    appserv = AppServers.objects.all().filter(servidor_id=id)   
    context = {'servidores': servidor, 'projetos': projeto, 'appservers': appserv}
    return render(request, 'servidores_detail.html', context)
"""