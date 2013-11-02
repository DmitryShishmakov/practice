from django.db import models
import datetime

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