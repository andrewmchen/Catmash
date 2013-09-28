from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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
        
    def is_valid(self):
        if self.password != self.verify:
            return False
        if '@' not in self.email:
            return False
        return True
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

        
        
