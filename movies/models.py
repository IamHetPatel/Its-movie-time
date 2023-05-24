from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    duration = models.PositiveIntegerField()
    rating = models.FloatField()

    def __str__(self):
        return self.title

class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    num_tickets = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.movie.title}'

class Seat(models.Model):
    row = models.CharField(max_length=1)
    number = models.PositiveIntegerField()
    booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.row}{self.number}"