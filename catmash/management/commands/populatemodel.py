from django.core.management.base import NoArgsCommand
from picture.models import pictures
import urllib2
import re

class Command(NoArgsCommand):
    help = 'Populates the database with images fetched online'
    def handle_noargs(self, **options):
        def fetchpictures(url):
            html=urllib2.urlopen(url).read()
            picturelist=re.findall(r'http://i.imgur.com.............',html)
            for picture in picturelist:
                p=pictures(url=picture,rating=1200)
                p.save()
        fetchpictures('http://imgur.com/r/cats')
