from django.db import models
import urllib2
import string
import re
# Create your models here.
class pictures(models.Model):
    url = models.CharField(max_length=40)
    rating = models.IntegerField()
    def __unicode__(self):
        return self.url+' rating of '+str(self.rating)
