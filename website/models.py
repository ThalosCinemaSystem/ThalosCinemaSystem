from django.db import models
from django.conf import settings

# Create your models here.
class Cinema(models.Model):
    city = models.CharField(max_length=30, null = True)
    street = models.CharField(max_length=30, null = True)
    country = models.CharField(max_length=30, null = True)
    name = models.CharField(max_length=30, null = True)
    address = models.CharField(max_length=30, null = True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=30, null = True)
    description = models.CharField(max_length=1024, null = True)
    during = models.IntegerField(null = True)
    thumbnail = models.CharField(max_length=30, null = True)
    genre = models.CharField(max_length=30, null = True)
    url_trailer = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title

class Room(models.Model):
    number = models.IntegerField(null=True)
    cinema_id = models.ForeignKey(Cinema, null= True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.number)

class Seat(models.Model):
    seat_number = models.IntegerField(null=True)
    number_of_column = models.IntegerField(null=True)
    number_of_row = models.IntegerField(null=True)
    room_id = models.ForeignKey(Room, null= True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.seat_number)

class Projection(models.Model):
    Type = (
        ('Lektor', 'Lektor'),
        ('Napisy', 'Napisy'),
        ('Dubbing','Dubbing'),
    )
    start_date_time = models.DateTimeField(null=True)
    is_3d = models.BooleanField(default=False)
    type_projection = models.CharField(max_length=200,null = True,choices = Type)
    price = models.FloatField(null=True)
    movie_id = models.ForeignKey(Movie, null= True, on_delete=models.CASCADE)
    room_id = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.movie_id.title

class Reservation(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
    seat_id = models.ForeignKey(Seat, null=True, on_delete=models.CASCADE)
    projection_id = models.ForeignKey(Projection, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_id.get_username()