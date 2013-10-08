from django.conf.urls import patterns,url


urlpatterns = patterns('',
    url(r'^$', 'catmash.views.rate'),
    url(r'^top$', 'catmash.views.top'),
    url(r'^toppic$', 'catmash.views.toppic')
    url(r'^trending$', 'catmash.views.top', { 'field': '-clicks'}),
    #url(r'^$',"picture.views.index")
)
