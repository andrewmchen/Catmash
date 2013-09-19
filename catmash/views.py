# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from catmash.models import pictures
from catmash.eloscript import adjust

import string
import random
import re
from catmash.models import pictures

def index(request):
    latest_picture_list = pictures.objects.all().order_by('?')[:2]
    picture1 = picture2 = 0
    while picture1 == picture2:
        picture2 = latest_picture_list[:1].get()
        picture1 = latest_picture_list[:1].get()
    template = loader.get_template('catmash/index.html/')
    print "index"
    context= { "picture1": picture1,"picture2":picture2}
    return render(request, 'catmash/index.html',context)
def top(request):
    number=10   #number of entries to display
    info = request.GET
    try: #try getting a number info item
        starting = int(info.__getitem__('number'))
        print starting
        pictures_by_rating = pictures.objects.order_by('rating')[starting:starting+10]
    except:
        print "did not get request"
        pictures_by_rating = pictures.objects.order_by('rating')[:10]
    context = { "pictures_by_rating": pictures_by_rating}
    return render(request, 'catmash/top.html', context)

def rate(request):
    info = request.GET
    print info.__getitem__('picture1')
    adjust(info.__getitem__('picture1'), info.__getitem__('picture2'))
    print info.__getitem__('picture1')
    return index(request)
