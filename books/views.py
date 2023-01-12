from django.shortcuts import render
from django.views.generic import *
from .models import *

# Create your views here.
class BookListView(ListView):
    template_name = "books/book_list.html"
    model = Book
    context_object_name = "book_list"


class BookDetailView(DetailView):
    template_name = "books/book_detail.html"
    model = Book
    context_object_name = "book"