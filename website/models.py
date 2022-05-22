from django.db import models
from django.contrib.auth.models import User
from azure.storage.blob import BlobClient
import os

try:
    os.environ["IS_PRODUCTION"]
except KeyError:
    pass
else:
    from TCS.settings import AZURE_CUSTOM_DOMAIN, AZURE_ACCOUNT_NAME
    from TCS.custom_azure import ACCOUNT_KEY


    def get_blob_service(container_name, blob_name):
        account_url = AZURE_CUSTOM_DOMAIN
        credential = {"account_name": AZURE_ACCOUNT_NAME,
                      "account_key": ACCOUNT_KEY}

        return BlobClient(account_url=account_url, credential=credential, container_name=container_name,
                          blob_name=blob_name)


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
    thumbnail = models.ImageField(upload_to='movies_images')
    url_trailer = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.title

    try:
        os.environ["IS_PRODUCTION"]
    except KeyError:
        pass
    else:
        def delete(self, *args, **kwargs):
            blob_service = get_blob_service(container_name='media', blob_name=self.thumbnail.name)
            blob_service.delete_blob()
            super(Movie, self).delete(*args, **kwargs)


class Genre(models.Model):
    names = (
        ('Dramat', 'Dramat'),
        ('Horror', 'Horror'),
        ('Akcji', 'Akcji'),
        ('Komedia', 'Komedia'),
        ('Romantyczny', 'Romantyczny'),
        ('Wojenny', 'Wojenny'),
        ('Kryminalny', 'Kryminalny'),
        ('Fantasy', 'Fantasy'),
        ('Sci-Fi', 'Sci-Fi'),
        ('Thriller', 'Thriller'),

    )
    name = models.CharField(max_length=20, null=True, choices=names)
    movie = models.ForeignKey(Movie, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


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
                         for seat_number in range(1, 26)]

            Seat.objects.bulk_create(seat_objs)

    def delete(self, *args, **kwargs):
        seats = Seat.objects.filter(room=self).all()
        seats.delete()
        super(Room, self).delete(*args, **kwargs)

    def __str__(self):
        return str(self.number)


class Seat(models.Model):
    seat_number = models.IntegerField(null=True)
    number_of_column = models.IntegerField(null=True)
    number_of_row = models.IntegerField(null=True)
    room = models.ForeignKey(Room, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(f'Seat Number: {self.seat_number} - Room Number: {self.room}')


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
