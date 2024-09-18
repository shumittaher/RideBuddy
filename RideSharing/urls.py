from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("mypage", views.mypage, name="mypage"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("make_trip", views.make_trip, name="make_trip"),
    path("find_trip", views.find_trip, name="find_trip"),
    # fetch queries
    path("give_trips", views.give_trips),
    path("give_bookingreq_forms/<int:trip_id>", views.give_bookingreq_forms),
    path("give_bookingreqs_list/<int:trip_id>", views.give_bookingreqs_list),
    path("booking_request", views.booking_request),
    path("give_unread", views.give_unread),
    path("messages_put", views.messages_put),
    path("delete_trip", views.delete_trip),
]