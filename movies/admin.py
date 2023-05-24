from django.contrib import admin
from .models import Movie
from .models import Booking
from .models import Seat

admin.site.register(Movie)

admin.site.register(Booking)
admin.site.register(Seat)
