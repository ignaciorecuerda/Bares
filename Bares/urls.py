from django.conf.urls import patterns, url
from Bares import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/$', views.about, name='about'),
        url(r'^register/$', views.register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^bar/(?P<bar_name_slug>\S+)$', views.bar, name='bar'),
        url(r'^add_bar/$', views.add_bar, name='add_bar'),
        url(r'^add_tapa/$', views.add_tapa, name='add_tapa'),
        url(r'^visitas/$', views.visitas, name='visitas'),
        url(r'^reclama_datos/$', views.reclama_datos, name='reclama_datos'),
        url(r'^megusta_tapa/$', views.megusta_tapa, name='megusta_tapa'),
       
#        url(r'^add_tapa/(?P<bar_name_slug>\w+)$', views.add_tapa, name='add_tapa'),               
        )


if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('', (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )

