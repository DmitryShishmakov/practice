from library.models import Author, Book, Publisher, BooksImage
from django.contrib import admin
from django.contrib.contenttypes import generic

class BooksImageAdmin(admin.ModelAdmin):
	list_display = ['book', 'preview', 'normal', 'count']

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)
admin.site.register(BooksImage, BooksImageAdmin)