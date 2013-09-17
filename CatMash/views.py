# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
import string
import random

from picture.models import pictures
def index(request):
    latest_picture_list=pictures.objects.all().order_by('?')[:2]
    picture2=latest_picture_list[:1].get()
    picture1=latest_picture_list[:1].get()
    print "hi"
    template=loader.get_template('picture/index.html/')
    context= { "picture1": picture1,"picture2":picture2}
    return render(request, 'picture/index.html',context)
def allah(request):
    info=request.GET
    f=open("debug.txt","a")
    print "allah"
    f.write(info+"\n")
    info=info[string.find(info,"?"):]
    f.write(info+"\n")
    f.close()
    return index(request)
