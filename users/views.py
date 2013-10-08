# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.shortcuts import render 
from django.contrib.auth import authenticate
from django.contrib.auth import login as loginmethod
from django.contrib.auth import logout as logoutmethod
from django.contrib.auth.models import User
from users.forms import UserCreateForm, LoginForm, UploadForm, UploadFile
from django.contrib.auth.decorators import login_required
from catmash.models import pictures

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        form = LoginForm(request.POST)
        form.is_valid()
        if user is not None:
            if user.is_active:
                loginmethod(request,user)
                print "logged in"
                return HttpResponseRedirect('/users/profile')
    else:
        form = LoginForm()
    return render(request,"registration/login.html", {'form':form})

def register(request):
    if request.method == 'POST':
        info = request.POST
        form = UserCreateForm(request.POST)
        if form.is_valid():
            print "Form is valid"
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            #new_user = User.objects.create_user(username=form.cleaned_data['username'],password = form.cleaned_data['password'], email = form.cleaned_data['email'])
            new_user = User(username = username, email = email)
            new_user.set_password(password)
            new_user.save()

            return HttpResponseRedirect("/users/login")
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
        form = UploadFile(request.POST, request.FILES)
        if form.is_valid():
            username = request.user.username
            print username+" has uploaded a picture"
            picture = pictures(username=username, name=request.POST['name'] ,rating=1200.0, clicks=0, image = request.FILES['file'])
            picture.save()
            return HttpResponseRedirect("/users/profile/")
    else:
        form = UploadFile()
    return render(request, "profile/upload.html", {'form':form})


"""def upload(request):
    ###################
    Old upload view new one will use files instead
    ###################
    if request.method == 'POST':
        url = request.POST['url']
        username = request.user.username
        name = request.POST['name']
        form = UploadForm(request.POST)
        if "http://" not in url:
            url = "http://"+url
        print url
        if form.is_valid():
            pictures.objects.create(url = url,name=name, username=username,rating = 1200.0, clicks=0)
            print "Uploaded"
            #redirect to success page
            return HttpResponseRedirect("/users/profile")
    else:
        form = UploadForm()
    return render(request, "profile/upload.html", {'form':form})
    
    """

            

    

@login_required

def profile(request):
    # see if the user has pictures 
    picture_list = list(pictures.objects.filter(username = request.user.username))
    url_list = []
    name_list = []
    rating_list = []
    for picture in picture_list:
        url_list+=[picture.url]
        name_list+=[picture.name]
        rating_list+=[picture.rating]

    picture_list = zip(url_list, name_list, rating_list)
    return render(request, "profile/index.html", {'username':request.user.username, 'picture_list':picture_list})
