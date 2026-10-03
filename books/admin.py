from django.contrib import admin
from .models import Book, Author, Rating, CustomUser

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Rating)
admin.site.register(CustomUser)
# Register your models here.
