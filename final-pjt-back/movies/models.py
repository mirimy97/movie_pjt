from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)


class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    genre = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=100)
    adult = models.BooleanField()
    poster_path = models.TextField()
    actor = models.TextField()
    overview = models.TextField()
    popularity = models.FloatField()
    release_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()

# id,title,adult,actors,overview,popularity,release_date,vote_average,vote_count

class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)