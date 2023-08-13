from django.db import models


class Actors(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    dob = models.DateField(max_length=200)
    address = models.CharField(max_length=200)
    contact = models.IntegerField()
    email = models.EmailField()

    def __str__(self) -> str:
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    buget = models.IntegerField(default=0)
    movie_release_location = models.CharField(max_length=200)
    release_date = models.DateField(max_length=200)
    actors = models.ManyToManyField(Actors)

    def __str__(self) -> str:
        return self.name





