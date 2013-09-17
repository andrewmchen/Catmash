from django.conf.urls import patterns,url


urlpatterns = patterns('',
    url(r'^$','picture.views.rate'),
    #url(r'^$',"picture.views.index")
)
