from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
import re


class UserCreateForm(forms.Form):

    username = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 30)
    verify = forms.CharField(max_length = 30)
    email = forms.CharField(max_length = 30)
    """def __init__(self,a,b,c,d):
        self.username = a
        self.password = b
        self.verify = c
        self.email = d
"""
    def initiate_with_args(self,a,b,c,d):
        self.username = a
        self.password = b
        self.verify = c
        self.email = d
    def clean_email(self):
        if '@' not in self['email']:
            raise forms.ValidationError("Looks like that's not a valid email")
    def clean_username(self):
        used = False
        try:
            form_username=self['username']
            print type(str(form_username).encode('utf8'))
            form_username = str(form_username).encode('utf8')
            form_username = re.findall('(?<=value=")(.*)(?=")',form_username)
            form_username = form_username[0]
            print form_username

            #piece of shit code to find value of username 

            User.objects.get(username = form_username)
            print "username used"
            used = True
        except User.DoesNotExist:
            pass
        if used:
            raise forms.ValidationError("Your username seems to be taken already")
        
    def save(self):
        new_user = User(username = self.username, email=self.email)
        new_user.set_password(self.password)
        new_user.save()
        return new_user


class LoginForm(forms.Form):
    username = forms.CharField(max_length = 30)
    password = forms.CharField(max_length = 30)
    def initiate_with_args(self,a,b):
        self.username = a
        self.password = b
    def clean(self):
        username = self['username']
        password = self['password']
        user = authenticate(username=username,password=password)
        if user is None:
            raise forms.ValidationError("It seems that your username/password pair doesn't match")


class UploadForm(forms.Form):
    url = forms.CharField(max_length = 100)
    name = forms.CharField(max_length = 20)
    def initiate_with_args(self,a,b):
        self.url=a
        self.name=b
    def clean_url(self):
        endings = [".png", ".jpg", ".jpeg", ".gif", ".tiff", ".bmp"]
        for end in endings:
            if end in self['url']:
                return True
        raise forms.ValidationError('Please put url of a picture (ends in .png/.jpg/etc...)')

        
        
