from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
from django.urls import reverse

class CustomUser(AbstractUser):
    pass
    def __str__(self):
        return f'{self.first_name} {self.last_name}' if self.first_name and self.last_name else self.username

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('books:author_book_list', kwargs={'pk': self.pk})
        
    @property
    def highest_rated_book(self):
        books = self.book_set
        # if books:
        #     highest_rated_book = books[0]
        #     for book in books:
        #         if book.score_avg > highest_rated_book.score_avg:
        #             highest_rated_book = book
        #     return highest_rated_book
        # else:
        #     return None
        return books.aggregate(models.Max('score_avg'))
                
        
        

class Book(models.Model):
    title = models.CharField(max_length=50, blank=False)
    title_long = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, blank=False)
    date_published = models.DateField()
    author = models.ManyToManyField(Author, blank=False)
    #score_avg = models.DecimalField(max_digits=3, decimal_places=2)

    GENRES = [
        ('SCIFI', 'Science Fiction'),
        ('ROM', 'Romance'),
        ('FAN', 'Fantasy'),
        ('BIO', 'Memoir and Biography'),
        ('CRIME', 'True Crime'),
        ('MYS', 'Mystery and Thriller'),
        ('HIS', 'Historical Fiction'),
    ]

    genre = MultiSelectField(choices=GENRES)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('books:book_detail', kwargs={'pk': self.pk})
        
    @property
    def score_avg(self):
        # score_sum = 0
        # for rating in self.rating_set.all():
        #     score_sum += rating.score
        # score_avg = score_sum / len(self.rating_set.all()) if self.rating_set.all() else 0
        # return score_avg
        return self.rating_set.aggregate(models.Avg('score', default=0))
        
def get_scores():
    return {i: i for i in range(0,6)}
    
class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    body = models.CharField(max_length=2000)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField(choices=get_scores, blank=False)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['book', 'user'], name='unique_rating')]

class UserBookStatus(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='users')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    class Status(models.TextChoices):
        WANT_TO_READ = 'W'
        READING = 'R'
        FINISHED = 'F'
        
    status = models.CharField(choices=Status, blank=False)


