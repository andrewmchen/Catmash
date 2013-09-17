from picture.models import pictures


def fetchpictures(url):
    html=urllib2.urlopen(url).read()
    picturelist=re.findall(r'http://i.imgur.com.............',html)
    for picture in picturelist:
        p=pictures(url=picture,rating=1200)
        p.save()
fetchpictures('http://imgur.com/r/cats')
