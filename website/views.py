from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render
from forms import UserCreateForm

def register(request):
    if request.method == 'POST':
        info = request.POST
        form = UserCreateForm()
        form.initiate_with_args(info.__getitem__('username'),info.__getitem__('password'),info.__getitem__('verify'),info.__getitem__('email'))
        if form.is_valid():
            print "Form is valid"
            new_user = form.save()
            return HttpResponseRedirect("/accounts/login")
        failed = True #makes a fail pop up
        print "Form Failed"
    else:
        failed = False
        form = UserCreateForm()
    return render(request, "registration/register.html", {'form':form,'failed':failed})
