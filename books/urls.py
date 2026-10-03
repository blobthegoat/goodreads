from django.urls import path
from books import views
app_name = 'books'

urlpatterns = [
    path('books/', views.BookListView.as_view(), name='homepage'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book_detail'),
    path('books/authors/<int:pk>', views.AuthorBookListView.as_view(), name='author_book_list' ),
    path('books/authors/', views.AuthorListView.as_view(), name='author_list'),
    path('signup/', views.UserSignup.as_view(), name='signup'),
    path('login', views.UserLogin.as_view(), name='login'),
    path('books/genre/<str:genre>/', views.BooksByGenreListView.as_view(), name='genre_list'),
    path('profile/', views.UserProfileView.as_view(), name='profile'),
    path('logout/', views.UserLogout.as_view(), name='logout'),
    
]