from .forms import BookingRequestCommentBox
from django.shortcuts import get_object_or_404
from .models import Trips, Spot_Bookings
from django.db.models import Sum


def make_booking_form(trip_id, user_id):

    trip = get_object_or_404(Trips, pk = trip_id)

    form = BookingRequestCommentBox(initial={
            'trip': trip_id,
            'requester': user_id,
        }, open_seats = trip.open_seats
    )

    return form

def find_remaining_spots(underlying_trip):

    total_approved_bookings = Spot_Bookings.objects.filter(trip = underlying_trip, approval_status = True).aggregate(Sum('spots_requested'))['spots_requested__sum']
    remaining_spots = underlying_trip.open_seats
    if total_approved_bookings:
        remaining_spots = underlying_trip.open_seats - total_approved_bookings
    return remaining_spots
    
def addremaining_spots(trips):
    
    trip_spot = []

    for trip in trips:
        open_spot = find_remaining_spots(trip)
        trip_spot.append({
            'trip': trip,
            'open_spot':open_spot
        })

    return trip_spot
