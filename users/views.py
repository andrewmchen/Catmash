# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render
from users.models import User

def signup(request):
    if request.method=='POST':
        info = request.POST
        new_user = User(username=info.__getitem__('username'),password=info.__getitem__('password'),email=info.__getitem__('email'))
        new_user.save()
        
    context = {}
    return render(request, 'users/signup.html', context)
