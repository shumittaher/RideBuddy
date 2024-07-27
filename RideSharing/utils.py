from .forms import BookingRequestCommentBox

def add_forms(trips, id):

    trips_forms= []

    for trip in trips:
        form = BookingRequestCommentBox(initial={
            'trip': trip.id,
            'requester': id,
        }, open_seats = trip.open_seats
        )

        trips_forms.append({'trip': trip, 'form': form})

    return trips_forms