from django.shortcuts import render
from .forms import UserCreateForm
from django.views.generic import FormView, ListView, DetailView
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from .models import Book, Author
# Create your views here.

class UserSignup(FormView):
    form_class = UserCreateForm
    success_url = reverse_lazy('books:login')
    template_name = 'books/signup.html'

class UserLogin(LoginView):
    template_name = 'books/login.html'
    next_page = reverse_lazy('books:homepage')

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'

class AuthorListView(ListView):
    model = Author
    template_name = 'books/author_list.html'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'books/author_detail.html'
    

    
        