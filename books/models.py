from django.db import models
from django.contrib.auth.models import AbstractUser
from multiselectfield import MultiSelectField
class CustomUser(AbstractUser):
    pass

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

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
        
    @property
    def score_avg(self):
        score_sum = 0
        for rating in self.objects.get(self.pk).rating_set:
            score_sum += rating.score
        score_avg = score_sum / len(self.objects.get(self.pk).rating_set)
        return score_avg
        
def get_scores():
    return {i: i for i in range(0,6)}
    
class Rating(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, blank=False)
    body = models.CharField(max_length=2000)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    score = models.IntegerField(choices=get_scores, blank=False)

class UserBookStatus(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='users')
    book = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Status(models.TextChoices):
        WANT_TO_READ = 'W'
        READING = 'R'
        FINISHED = 'F'
        
    status = models.CharField(choices=Status, blank=False)


