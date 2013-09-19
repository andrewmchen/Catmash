from django.conf.urls import patterns, include, url
import os

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', include('picture.urls')),
    url(r'^catmash', include('catmash.urls')), #ajax fetch link
    url(r'^top','catmash.views.top'),
    url(r'^trending$', 'catmash.views.top', { 'field': '-clicks'}),
    url(r'^static/(?P<path>.*)$',
        'django.views.static.serve',
        {'document_root': os.getenv('STATIC_DIR')}
    ),
    url(r'^$', 'catmash.views.index')


    # url(r'^CatMash/', include('CatMash.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
