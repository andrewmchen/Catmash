from django.conf.urls import patterns,url
import views

urlpatterns = patterns('',url(r'^picture$','views.allah'),url(r'^$',"views.index"))
