from django.db import models
import urllib2
import string
import re
# Create your models here.
class pictures(models.Model):
    url = models.CharField(max_length=40)
    rating = models.DecimalField(max_digits=10, decimal_places=5)
    def __unicode__(self):
        return self.url+' rating of '+str(self.rating)
