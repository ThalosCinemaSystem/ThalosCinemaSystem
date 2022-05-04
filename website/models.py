from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cinema(models.Model):
    city = models.CharField(max_length=30, null=True)
    street = models.CharField(max_length=30, null=True)
    country = models.CharField(max_length=30, null=True)
    name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=1024, null=True)
    during = models.IntegerField(null=True)
    thumbnail = models.ImageField(null = True, blank = True)
    genre = models.CharField(max_length=30, null=True)
    url_trailer = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title


class Room(models.Model):
    number = models.IntegerField(null=True)
    cinema = models.ForeignKey(Cinema, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)


class Seat(models.Model):
    seat_number = models.IntegerField(null=True)
    number_of_column = models.IntegerField(null=True)
    number_of_row = models.IntegerField(null=True)
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.seat_number)


class Projection(models.Model):
    types = (
        ('Lektor', 'Lektor'),
        ('Napisy', 'Napisy'),
        ('Dubbing', 'Dubbing'),
    )
    start_date_time = models.DateTimeField(null=True)
    is_3d = models.BooleanField(default=False)
    type_projection = models.CharField(max_length=200, null=True, choices=types)
    price = models.FloatField(null=True)
    movie = models.ForeignKey(Movie, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.title


class Reservation(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, null=True, on_delete=models.CASCADE)
    projection = models.ForeignKey(Projection, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_username()


class Marathon(models.Model):
    name = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=1024, null=True)
    price = models.FloatField(null=True)
    thumbnail = models.ImageField(null=True, blank=True)
