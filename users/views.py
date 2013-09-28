# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render 
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginmethod
from django.contrib.auth import logout as logoutmethod


from users.forms import UserCreateForm, LoginForm, UploadForm
from django.contrib.auth.decorators import login_required
from catmash.models import pictures


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                loginmethod(request,user)
                print "logged in"
                return HttpResponseRedirect('/users/profile')
    form = LoginForm()
    return render(request,"registration/login.html", {'form':form})

def register(request):
    if request.method == 'POST':
        info = request.POST
        form = UserCreateForm()
        form.initiate_with_args(info.__getitem__('username'),info.__getitem__('password'),info.__getitem__('verify'),info.__getitem__('email'))
        if form.is_valid():
            print "Form is valid"
            new_user = form.save()
            return HttpResponse.HttpResponseRedirect("/users/login")
        failed = True #makes a fail pop up
        print "Form Failed"
    else:
        failed = False
        form = UserCreateForm()
    return render(request, "registration/register.html", {'form':form,'failed':failed})


def logout(request):
    logoutmethod(request)
    return HttpResponseRedirect("/")

def upload(request):
    if request.method == 'POST':
        url = request.POST['url']
        username = request.user.username
        name = request.POST['name']
        form = UploadForm(request.POST)
        if form.is_valid():
            pictures.objects.create(url = url,name=name, username=username,rating = 1200.0, clicks=0)
            print "Uploaded"
            #redirect to success page
    else:
        form = UploadForm()
    return render(request, "profile/upload.html", {'form':form})

            

    

@login_required

def profile(request):
    # see if the user has pictures 
    number_of_pictures=pictures.objects.all().filter(username=request.user.username).count()
    has_pictures=True
    if number_of_pictures == 0:
        has_pictures=False
    cat = pictures.objects.all().filter(username = request.user.username)[:1].get()
    url = cat.url
    name = cat.name
        


    return render(request, "profile/index.html", {'username':request.user.username,'has_pictures':has_pictures,'url':url,'name':name})
