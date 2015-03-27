"""
class ServerAdmin(admin.ModelAdmin):

    Customize the look of the auto-generated admin for the Member model
    list_display = ('nome', 'nome')
    list_filter = ('ambiente',)
"""

from django.contrib import admin

from .models import Projetos, Servidores


admin.site.register(Projetos)  # Use the default options
admin.site.register(Servidores)  # Use the customized options