from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import *
from .models import *
from django.db.models import Q

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


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"

    def get_queryset(self):
        return Book.objects.filter(
            Q(title__icontains="beginners") | Q(title__icontains="api")
        )