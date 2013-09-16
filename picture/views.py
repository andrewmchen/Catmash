# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
import random

from picture.models import pictures
def index(request):
    latest_picture_list=pictures.objects.all().order_by('?')[:2]
    template=loader.get_template('picture/index.html/')
    context= { "latest_picture_list": latest_picture_list}
    return render(request, 'picture/index.html',context)
