from django.conf.urls import patterns,url


urlpatterns = patterns('',
    url(r'^$','catmash.views.rate'),
    #url(r'^$',"picture.views.index")
)
