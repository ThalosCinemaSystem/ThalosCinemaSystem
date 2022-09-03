from django.db import models
from django.contrib.auth.models import User
from datetime import timedelta


class Cinema(models.Model):
    city = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=1024, null=True)
    during = models.IntegerField(null=True)
    thumbnail = models.ImageField(upload_to='upload_thumbnails')
    url_trailer = models.CharField(max_length=255, null=True)
    genre = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title


class Room(models.Model):
    number = models.IntegerField(null=True)
    cinema = models.ForeignKey(Cinema, null=True, on_delete=models.CASCADE)

    def save(self, *args, **kwargs):
        if not Seat.objects.filter(room=self):
            super(Room, self).save(*args, **kwargs)
            seat_objs = [Seat(seat_number=seat_number,
                              number_of_row=None,
                              number_of_column=None,
                              room=self)
                         for seat_number in range(0, 100)]

            Seat.objects.bulk_create(seat_objs)

    def delete(self, *args, **kwargs):
        seats = Seat.objects.filter(room=self).all()
        seats.delete()
        super(Room, self).delete(*args, **kwargs)

    def __str__(self):
        return f'Numer sali: {str(self.number)} - Kino: {self.cinema.name} - Miasto: {self.cinema.city}'


class Seat(models.Model):
    seat_number = models.IntegerField(null=True)
    number_of_column = models.IntegerField(null=True)
    number_of_row = models.IntegerField(null=True)
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)
    is_durning_reservation = models.BooleanField(default=False)

    def __str__(self):
        return str(f'Seat Number: {self.seat_number} - Room Number: {self.room}')

    @property
    def is_reservated(self):
        if Reservation.objects.filter(seat_id=self).first():
            return True
        return False


class Marathon(models.Model):
    name = models.CharField(max_length=30, null=True)
    description = models.CharField(max_length=1024, null=True)
    price = models.FloatField(null=True)
    thumbnail = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}'


class Projection(models.Model):
    types = (
        ('Lektor', 'Lektor'),
        ('Napisy', 'Napisy'),
        ('Dubbing', 'Dubbing'),
    )
    start_date_time = models.DateTimeField(null=True)
    is_3d = models.BooleanField(default=False)
    type_projection = models.CharField(max_length=20, null=True, choices=types)
    price = models.FloatField(null=True)
    movie = models.ForeignKey(Movie, null=True, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)
    marathon = models.ForeignKey(Marathon, blank=True, null=True, on_delete=models.CASCADE)
    is_cyclic = models.BooleanField(default=False, null=True)

    def __str__(self):
        return f'{self.movie.title} - {self.start_date_time} - Room: {self.room.number} - IS_CYCLIC: {self.is_cyclic}'

    def save(self, *args, **kwargs):
        if self.is_cyclic:
            projections = [Projection(start_date_time=self.start_date_time + timedelta(weeks=i),
                                      is_3d=self.is_3d,
                                      type_projection=self.type_projection,
                                      price=self.price,
                                      movie=self.movie,
                                      room=self.room,
                                      marathon=self.marathon,
                                      is_cyclic=self.is_cyclic)
                           for i in range(0, 10)]
            Projection.objects.bulk_create(projections)
        else:
            super(Projection, self).save(*args, **kwargs)


class Reservation(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, null=True, on_delete=models.CASCADE)
    projection = models.ForeignKey(Projection, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_username()
