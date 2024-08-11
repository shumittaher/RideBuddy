from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.utils import timezone
from django.template.loader import render_to_string
from django.contrib import messages

import json

from .models import User, Trips, Spot_Bookings
from .forms import TripsForm, LocationSearchForm, BookingRequestCommentBox
from .utils import add_forms

# Create your views here.

def login_view(request):

    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "register.html")

def index(request):
    return render(request, "index.html")

def make_trip(request):

    active_user = get_object_or_404(User, pk = request.user.id)

    if request.method == "POST":

        new_trip_form = TripsForm(request.POST)
        if new_trip_form.is_valid():
            new_trip_form.cleaned_data["trip_owner"] = active_user
            TripsForm(new_trip_form.cleaned_data).save()

    inital_form = TripsForm(initial={
        'trip_owner' : active_user
    }).render("form_snippets/form.html")
    today = timezone.now().date()
    trips = Trips.objects.filter(valid_till__gte=today, trip_owner_id = request.user.id)
    my_active_trips = add_forms(trips, request.user.id, False)

    return render(request, "make_trip.html", {
        'trip_form': inital_form,
        'my_active_trips': my_active_trips
    })

def find_trip(request):

    search_form = LocationSearchForm().render("form_snippets/form.html")

    return render(request, "find_trip.html", {
        'search_form': search_form,
    })

def give_trips(request):

    if request.method == 'GET':
        origin_area = request.GET.get('origin_area', '')

        if origin_area:
            queryset = Trips.objects.filter(origin=origin_area)
        else:
            queryset = Trips.objects.all()

        trips_and_forms = add_forms(queryset, request.user.id, True)

        rendered_trips = render_to_string('component_snippets/trips_list.html', {'trips': trips_and_forms})
        return JsonResponse({'rendered_trips': rendered_trips})
    
def booking_request(request):

    if request.method == 'POST':
        new_booking_data = json.loads(request.body)['booking_request']

        new_booking = BookingRequestCommentBox(new_booking_data)

        if new_booking.is_valid():
            new_booking.save()
            messages.success(request, "Booking request recorded successfully.")
            return JsonResponse({"status": "Booking data saved"}, status=200)

        else:
            return JsonResponse({"status": "Invalid booking data"}, status=400)


