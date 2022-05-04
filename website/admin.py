from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Cinema)
admin.site.register(Room)
admin.site.register(Seat)
admin.site.register(Reservation)
admin.site.register(Projection)
admin.site.register(Movie)
admin.site.register(Marathon)
