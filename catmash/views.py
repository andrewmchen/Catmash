# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
import string
import random
import re

from catmash.models import pictures
def index(request):
    latest_picture_list=pictures.objects.all().order_by('?')[:2]
    picture2=latest_picture_list[:1].get()
    picture1=latest_picture_list[:1].get()
    template=loader.get_template('catmash/index.html/')
    print "index"
    context= { "picture1": picture1,"picture2":picture2}
    return render(request, 'catmash/index.html',context)
def rate(request):
    def adjust(winner,loser): #parameters are the urls
        winner_object=pictures.objects.filter(url=winner)[0]
        loser_object=pictures.objects.filter(url=loser)[0]
        winner_rating=winner_object.rating
        loser_rating=loser_object.rating
        winner_expected=1.0/(1+10**((loser_rating-winner_rating)/400))
        loser_expected=1.0/(1+10**((winner_rating-loser_rating)/400))
        winner_new=winner_rating+32*(1-winner_expected)
        loser_new=loser_rating+32*(0-loser_expected)
        winner_object.rating=winner_new
        loser_object.rating=loser_new
        print winner_new
        print loser_new
        winner_object.save()
        loser_object.save()
    info=request.GET
    
    print info.__getitem__('picture1')
    adjust(info.__getitem__('picture1'),info.__getitem__('picture2'))
    return index(request)
