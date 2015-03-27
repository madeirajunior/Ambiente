from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^proj/(?P<pk>\d+)/$', 'Banksphere.views.proj', name='proj'),
    url(r'^$', 'Banksphere.views.lista_proj', name='lista_proj'),
    #url(r'^serv/(?P<id>\d+)/$', 'Banksphere.views.serv', name='proj'),
    #url(r'^proj/(?P<pk>\d+)/(?P<id>\d+)/$', 'Banksphere.views.proj', name='proj'),
    #url(r'^appserv_detail/(?P<pk>\d+)/$', 'Banksphere.views.appserv_detail', name='appserv_detail'),
)
