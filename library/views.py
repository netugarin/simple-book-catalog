from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.views import generic

from .forms import BookForm, AuthorForm
from .models import Book, Author


class BookListView(generic.ListView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author


def index(request):
    books = Book.objects.all()
    return render(request, 'index.html', {'books': books},)


def book_new(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return HttpResponseRedirect('/')
    else:
        form = BookForm()
    return render(request, 'library/book_edit.html', {'form': form})


def author_new(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = form.save()
            author.save()
            return HttpResponseRedirect('/authors')
    else:
        form = AuthorForm()
    return render(request, 'library/author_edit.html', {'form': form})


def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    if request.method == 'POST':
        book.delete()
        return HttpResponseRedirect('/')

    return render(request, 'library/book_list.html', {'book': book})


def author_delete(request, pk):
    author = get_object_or_404(Author, pk=pk)

    if request.method == 'POST':
        author.delete()
        return HttpResponseRedirect('/authors')

    return render(request, 'library/author_list.html', {'author': author})
