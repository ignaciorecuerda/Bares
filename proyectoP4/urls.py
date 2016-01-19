from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings # New Import
from django.conf.urls.static import static # New Import
from registration.backends.simple.views import RegistrationView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
	def get_success_url(self,request, user):
		return '/Bares/'

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	
	url(r'^admin/', include(admin.site.urls)),
	url(r'^Bares/', include('Bares.urls')), # ADD THIS NEW TUPLE!media/(?P<path>.*) cambiado el taaaab
)

if not settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )

if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(r'^media/(?P<path>.*)',
		'serve',
		{'document_root': settings.MEDIA_ROOT}), )
