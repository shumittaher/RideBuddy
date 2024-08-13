from .forms import BookingRequestCommentBox
from django.shortcuts import get_object_or_404
from .models import Trips


def make_booking_form(trip_id, user_id):

    trip = get_object_or_404(Trips, pk = trip_id)

    form = BookingRequestCommentBox(initial={
            'trip': trip_id,
            'requester': user_id,
        }, open_seats = trip.open_seats
    )

    return form

