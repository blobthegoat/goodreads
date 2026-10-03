from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .forms import UserCreateForm, ReviewForm
from django.views.generic import FormView, ListView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, reverse_lazy
from .models import Book, Author, CustomUser
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
# Create your views here.

class UserSignup(FormView):
    form_class = UserCreateForm
    success_url = reverse_lazy('books:login')
    template_name = 'books/signup.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class UserLogin(LoginView):
    template_name = 'books/login.html'
    next_page = reverse_lazy('books:homepage')

class BookListView(ListView):
    model = Book
    template_name = 'books/book_list.html'

class BookDetailView(DetailView, FormMixin):
    model = Book
    template_name = 'books/book_detail.html'
    form_class = ReviewForm
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Book.objects.get(pk=self.kwargs['pk']).rating_set.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
        
    def post(self, request, *args, **kwargs):
        self.success_url = reverse_lazy('books:book_detail', kwargs={'pk': self.kwargs['pk']})
        form = self.get_form()
        if form.is_valid():
            form.instance.book = Book.objects.get(pk=self.kwargs['pk'])
            form.instance.user = self.request.user
            return self.form_valid(form)
            
        return self.form_invalid(form)

class AuthorBookListView(ListView):
    model = Book
    template_name = 'books/author_book_list.html'
    context_object_name = 'books_by_author'

    def get_queryset(self):
        queryset = Book.objects.filter(author__pk=self.kwargs['pk'])
        return queryset

    

class AuthorListView(ListView):
    model = Author
    template_name = 'books/author_list.html'

    # def get_context_data(self,**kwargs):
    #     context = super().get_context_data(**kwargs)
    #     cont
    #     return context

class BooksByGenreListView(ListView):
    template_name = 'books/genre_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        books_by_genre = Book.objects.filter(genre__contains=self.kwargs['genre'])
        return books_by_genre

class UserProfileView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'books/profile.html'
    context_object_name = 'user'

    def get_object(self):
        return self.request.user

class UserLogout(LogoutView):
    template_name = 'books/book_list.html'
            
    
    
        