from django.db import models
import urllib2
import string
import re
# Create your models here.
class pictures(models.Model):
    url = models.CharField(max_length=40)
    image = models.ImageField(upload_to = 'images/%Y/%m/%d/')
    rating = models.DecimalField(max_digits=10, decimal_places=5)
    clicks = models.IntegerField()
    username = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    def __unicode__(self):
        return self.url+' rating of '+str(self.rating)
