from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import *
from .models import *

# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    template_name = "books/book_list.html"
    model = Book
    context_object_name = "book_list"
    login_url = "account_login"


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = "books/book_detail.html"
    model = Book
    context_object_name = "book"
    login_url = "account_login"
    permission_required = "books.special_status"