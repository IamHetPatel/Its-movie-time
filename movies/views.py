from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Movie, Booking, Seat
from .forms import BookingForm
from django.db.models import Count
from django.http import JsonResponse

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

@login_required
def seat_list(request):
    seats = Seat.objects.all()
    data = [{'row': seat.row, 'number': seat.number, 'status': seat.booked} for seat in seats]
    return JsonResponse(data, safe=False)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('movie_list')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('movie_list')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('movie_list')


def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies})

@login_required
def book_ticket(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            num_tickets = form.cleaned_data['num_tickets']
            user = request.user

            # Check if the user has exceeded the ticket booking limit
            bookings_count = Booking.objects.filter(user=user, date__month=date.month).count()
            if bookings_count + num_tickets > 2:
                return render(request, 'booking_error.html')

            # Save the booking
            booking = Booking(movie=movie, user=user, date=date, num_tickets=num_tickets)
            booking.save()
            return redirect('booking_confirmation')

    else:
        form = BookingForm()

    return render(request, 'book_ticket.html', {'movie': movie, 'form': form})

@login_required
def booking_confirmation(request):
    return render(request, 'booking_confirmation.html')

@login_required
def seat_map(request):
    seats = Seat.objects.all()
    return render(request, 'seat_map.html', {'seats': seats})

@login_required
def book_seat(request):
    if request.method == 'POST':
        seat_id = request.POST.get('seat')
        seat = Seat.objects.get(id=seat_id)
        if seat.booked:
            # Seat already booked
            return redirect('seat_map')
        else:
            seat.booked = True
            seat.save()
            return redirect('booking_confirmation.html')
    else:
        return redirect('movie_list')
