from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'Ambiente.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^proj_detail/(?P<pk>\d+)/$', 'Banksphere.views.proj_detail', name='proj_detail'),
    #url(r'^appserv_detail/(?P<pk>\d+)/$', 'Banksphere.views.appserv_detail', name='appserv_detail'),
    url(r'^$', 'Banksphere.views.lista_proj', name='lista_proj'),
)
