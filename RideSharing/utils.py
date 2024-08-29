from .forms import BookingRequestCommentBox
from django.shortcuts import get_object_or_404
from .models import Trips, Spot_Bookings, Messages
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

def send_message(message_data):
              
    if message_data["message_type"] == 'approval':
        content = f"Your Request for {message_data['underlying_trip']} is now approved"

    if message_data["message_type"] == 'request':
        content = f'New booking request received for {message_data["underlying_trip"]}'

    if message_data["message_type"] == 'rejection':
        content = f'Your Request for {message_data["underlying_trip"]} has been rejected'

    message_data['content'] = content

    new_message = Messages(**message_data)
    new_message.save()
