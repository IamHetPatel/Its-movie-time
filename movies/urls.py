from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('book-ticket/<int:movie_id>/', views.book_ticket, name='book_ticket'),
    path('confirmation/', views.booking_confirmation, name='booking_confirmation'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('seat-map/', views.seat_map, name='seat_map'),
    path('book-seat/', views.book_seat, name='book_seat'),
    path('seats/', views.seat_list, name='seat_list'),
]