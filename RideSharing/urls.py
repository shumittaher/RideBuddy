from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("make_trip", views.make_trip, name="make_trip"),
    path("find_trip", views.find_trip, name="find_trip"),
    # fetch queries
    path("give_trips", views.give_trips),
    path("booking_request", views.booking_request)
]