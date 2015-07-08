from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls import patterns

urlpatterns = [
    # Examples:
    # url(r'^$', 'cardom_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('cardom.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )