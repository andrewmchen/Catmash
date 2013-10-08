# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from catmash.models import pictures
from catmash.eloscript import adjust, agree

import string
import random
import re
from catmash.models import pictures

def index(request, extra=0):
    latest_picture_list = pictures.objects.all().order_by('?')[:2]
    picture1 = picture2 = 0
    while picture1 == picture2:
        picture2 = latest_picture_list[:1].get()
        picture1 = latest_picture_list[:1].get()
    template = loader.get_template('catmash/index.html/')
    try:
        ###Generate how many people agree with you.
        info = request.GET
        people_who_agree = agree(info.__getitem__('picture1'), info.__getitem__('picture2'))
        ###
        last_win_picture = pictures.objects.filter(url=info.__getitem__('picture1'))[0] ###Finds the picture that you last clicked
        clicks = last_win_picture.clicks
        context = { "picture1": picture1,
                    "picture2": picture2,
                    "people_who_agree": people_who_agree,
                    "clicks": clicks,
                    "data": extra}
        return render(request, 'catmash/indexwithclicks.html', context)
    except:
        context = {"picture1": picture1, "picture2" :picture2}
        return render(request, 'catmash/index.html', context)

def top(request, field='-rating'):
    number=10   #number of entries to display
    info = request.GET
    try: #try getting a number info item
        starting = int(info.__getitem__('number'))
        print starting
        pictures_by_rating = pictures.objects.order_by(field)[starting:starting+10]
    except:
        print "did not get request"
        pictures_by_rating = pictures.objects.order_by(field)[:10]
    context = { "pictures_by_rating": enumerate(pictures_by_rating)}
    return render(request, 'catmash/top.html', context)

def rate(request):
    info = request.GET
    print info.__getitem__('picture1')
    winner, loser, delta = adjust(info.__getitem__('picture1'), info.__getitem__('picture2')) #change the ratings
    print info.__getitem__('picture1')

    #add 1 click to each picture
    picture1 = pictures.objects.filter(url = info.__getitem__('picture1'))[0]
    picture2 = pictures.objects.filter(url = info.__getitem__('picture2'))[0]
    ###Adding 1 click each
    picture1.clicks += 1
    picture2.clicks += 1
    picture1.save()
    picture2.save()

    return index(request, "%s,%s,%s" %(winner, loser, delta))
