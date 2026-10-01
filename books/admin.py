from django.contrib import admin
from .models import Book, Author, Rating

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Rating)
# Register your models here.
