# -*- coding: utf8 -*-
from django.shortcuts import render
from library.models import Author
from library.models import Book

def books(request):
  context = {'books': Book.objects.all()}
  return render(request, 'books.html', context)


def book(request, idBook):
  context = {'book': Book.objects.get(id = idBook)}
  return render(request, 'book.html', context)

def authors(request):
  context = {'authors': Author.objects.all()}
  return render(request, 'authors.html', context)


def author(request, idAuthor):
  context = {'author': Author.objects.get(id = idAuthor)}
  return render(request, 'author.html', context)