from .forms import BookingRequestCommentBox

def add_forms(trips, id, addform):

    trips_forms= []

    for trip in trips:
        form = BookingRequestCommentBox(initial={
            'trip': trip.id,
            'requester': id,
        }, open_seats = trip.open_seats
        )

        if addform:
            trips_forms.append({'trip': trip, 'form': form})
        else:
            trips_forms.append({'trip': trip})

    return trips_forms

