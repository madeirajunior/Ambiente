from django.shortcuts import render, render_to_response
from .models import Projetos, Servidores

"""
def lista_proj(request):
    lista_projetos = Projetos.objects.all()
    return render_to_response("lista_projetos.html", {'lista_projetos': lista_projetos})
"""
def lista_proj(request):
    """ A view of all bands. """
    proj = Projetos.objects.all()
    var_get_search = request.GET.get('search_box')
    if var_get_search is None:
        proj = proj.filter(nome__icontains=var_get_search)
    return render(request, 'lista_projetos.html', {'proj': proj})


def proj_detail(request, pk):
    """ A view of all members by bands. """
    proj = Projetos.objects.get(pk=pk)
    serv = Servidores.objects.all().filter(proj=proj)
    context = {'servidores': serv, 'projetos': proj}
    return render(request, 'servidores_detail.html', context)