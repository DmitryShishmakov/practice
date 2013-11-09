from django.db import models
import datetime
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length = 32)
    last_name = models.CharField(max_length = 32)
    email = models.EmailField(null = True, blank = True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)


class Book(models.Model):
    title = models.CharField(max_length = 128)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey('Publisher')
    publication_date = models.DateField(default=datetime.datetime.now())

    def __unicode__(self):
        return self.title


class Publisher(models.Model):
    title = models.CharField(max_length = 32)
    address = models.TextField()
    city = models.CharField(max_length = 64)
    country = models.CharField(max_length = 64)
    website = models.URLField(max_length = 32)

    def __unicode__(self):
        #return u'%s (%s)'%(self.title, self.website)
        return u'%s (%s, %s)'%(self.title, self.city, self.country)

class BooksImage(models.Model):
    preview = models.ImageField(upload_to = "images/preview")
    normal = models.ImageField(upload_to = "images/normal", null = True, blank = True)
    contentType = models.ForeignKey(ContentType)
    contentObj = generic.GenericForeignKey("contentType", "objId")
    book = models.ForeignKey(Book)

    def getcover(self):
        return self.__cover

    def setcover(self, cover):
        self.__cover = cover
    
    cover = property(getcover, setcover)

    def __unicode__(self):
        return u'%s' % self.book

    def count(self):
        cnt=0
        if self.small:
            cnt += 1
        if self.big:
            cnt += 1
        return(cnt)
    