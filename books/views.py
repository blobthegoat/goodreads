from django.shortcuts import render
from .forms import UserCreateForm
from django.views.generic import FormView, ListView, DetailView
from django.contrib.auth.views import LoginView
from django.urls import reverse, reverse_lazy
from .models import Book, Author
from django.views.generic.edit import FormMixin
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Book.objects.get(pk=self.kwargs['pk']).rating_set.all()
        return context

class AuthorListView(ListView):
    model = Author
    template_name = 'books/author_list.html'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'books/author_detail.html'
    

    
        