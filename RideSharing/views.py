from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.utils import timezone
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


import json

from .models import User, Trips, Spot_Bookings, Messages
from .forms import TripsForm, LocationSearchForm, BookingRequestCommentBox
from .utils import make_booking_form, find_remaining_spots, addremaining_spots, send_message

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

@login_required(login_url ='/login')
def mypage(request):

    page_no_unread = request.GET.get('page_no_unread', 1)
    page_no_read = request.GET.get('page_no_read', 1)
    active_side = request.GET.get('active_side', 'unread')
    items_per_page = request.GET.get('items_per_page', 10)
    user_id = request.user.id
    user = User.objects.get(id=user_id)

    unread_paginator = Paginator(user.message_recipient.filter(read = False).order_by('-time_stamp'), items_per_page)
    read_paginator = Paginator(user.message_recipient.filter(read = True).order_by('-time_stamp'), items_per_page)

    unread_messages = unread_paginator.get_page(page_no_unread)
    read_messages = read_paginator.get_page(page_no_read)

    return render(request, "mypage.html", {
        'recipient' : user,
        'unread_messages' : unread_messages,
        'read_messages' : read_messages,
        'active_side': active_side
    })

@login_required(login_url ='/login')
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
    my_active_trips = Trips.objects.filter(valid_till__gte=today, trip_owner_id = request.user.id)

    my_active_trips_spots = addremaining_spots(my_active_trips)

    return render(request, "make_trip.html", {
        'trip_form': inital_form,
        'my_active_trips': my_active_trips_spots
    })

def find_trip(request):

    search_form = LocationSearchForm().render("form_snippets/form.html")

    return render(request, "find_trip.html", {
        'search_form': search_form,
    })

def give_trips(request):

    if request.method == 'GET': 
        
        info_only = request.GET.get('info_only') == 'true'
        booking_trips = request.GET.get('booking_trips') == 'true'
        trip_id = request.GET.get('trip_id')
        spec_booking = request.GET.get('spec_booking')
        
        if trip_id:
            queryset = [Trips.objects.get(id = trip_id)]            # specific trip
        
        else:                                                       # filter process
            filter_dict = {}
            origin_area = request.GET.get('origin_area', '')
            destination_area = request.GET.get('destination_area', '')
            active_only = request.GET.get('active_only', True)
            
            queryset = Trips.objects.all()

            if origin_area:
                filter_dict["origin__location_area"] = origin_area
            
            if destination_area:
                filter_dict["destination__location_area"] = destination_area
 
            if active_only:
                today = timezone.now().date()
                filter_dict["valid_till__gte"] = today

            queryset = queryset.filter(**filter_dict)
        
        trips = addremaining_spots(queryset)                        # add remaining spots to the tripset
        
        if not info_only:
            rendered_trips = render_to_string('component_snippets/trips_list.html', {
                'trips': trips,
                'booking_trips': booking_trips,
                'spec_booking' : spec_booking,
                })
            
        else:
            if spec_booking:
                status = Spot_Bookings.objects.get(pk = spec_booking).approval_status
            else:
                status = None
            rendered_trips = render_to_string('component_snippets/trips_list_info.html', {
                'trips': trips,
                'booking_trips': booking_trips,
                'status' : status
                })
            
        return JsonResponse({'rendered_trips': rendered_trips})
    
def booking_request(request):

    if request.method == 'PUT':
        put_data = json.loads(request.body)
        req_id = put_data['req_id']
        save_action = put_data['save_action']

        underlying_booking = Spot_Bookings.objects.get(id=req_id)
        underlying_trip = underlying_booking.trip

        message_data = {
            'recipient': underlying_booking.requester,
            'underlying_trip' : underlying_trip,
            'underlying_booking' : underlying_booking,
        }

        if save_action:
            remaining_spots = find_remaining_spots(underlying_trip)
            required_spots = underlying_booking.spots_requested 
            if underlying_booking.approval_status:
                required_spots = 0

            if (remaining_spots - required_spots) >= 0:
                underlying_booking.approval_status = True
                underlying_booking.save()

                message_data['message_type'] = 'approval'  
                send_message(message_data)
                
                return JsonResponse({
                    "message": "Approved", 
                    "open_spots" : find_remaining_spots(underlying_trip),
                    "status": "saved"
                    })
            else:
                return JsonResponse({
                    "message": "Insuffcient Seats", 
                    "open_spots" : find_remaining_spots(underlying_trip),
                    "status": "warning"
                    })
        
        else:

            message_data['message_type'] = 'rejection'  
            send_message(message_data)

            underlying_booking.delete()

            return JsonResponse({
                "message": "Deleted", 
                "open_spots" : find_remaining_spots(underlying_trip),
                "status": "deleted"
            }) 

    elif request.method == 'POST':
        new_booking_data = json.loads(request.body)['booking_request']

        new_booking = BookingRequestCommentBox(new_booking_data)

        if new_booking.is_valid():

            new_booking_instance = new_booking.save()

            message_data = {
                'recipient': new_booking.cleaned_data["trip"].trip_owner,
                'underlying_trip' : new_booking.cleaned_data["trip"],
                'underlying_booking' : new_booking_instance,
                'message_type': 'request'
            }

            send_message(message_data)
           
            messages.success(request, "Booking request recorded successfully.")
            return JsonResponse({"status": "Booking data saved"}, status=200)

        else:
            return JsonResponse({"status": "Invalid booking data"}, status=400)

def give_bookingreq_forms(request, trip_id):

    form = make_booking_form(trip_id, request.user.id)

    rendered_form = render_to_string('component_snippets/booking_request_form.html', {
        'form': form,
    })

    return JsonResponse({"rendered_form": rendered_form}, status = 200)

def give_bookingreqs_list(request, trip_id):

    underlying_trip = Trips.objects.get(id = trip_id)
        
    filter_dict = {
        'trip' : underlying_trip
    }

    spec_booking = request.GET.get('spec_booking')
    
    if spec_booking:
        filter_dict['id'] = spec_booking

    bookingreq_list = Spot_Bookings.objects.filter(**filter_dict)

    rendered_form = render_to_string('component_snippets/bookingreq_list.html', {
        'bookingreq_list': bookingreq_list,
        'trip_id': trip_id,
    })

    return JsonResponse({"rendered_form": rendered_form}, status = 200)
    
def give_unread(request):

    unread_number = Messages.objects.filter(recipient = request.user, read = False).count()

    if unread_number > 99:
        unread_number = '99+'

    return JsonResponse({
        "unread": unread_number
    })

def messages_put(request):

    if request.method == 'PUT':
        put_data = json.loads(request.body)

    msg_id = put_data["message_id"]

    message = Messages.objects.get(id = msg_id)
    message.read = True

    message.save()

    return JsonResponse({
            'id': message.id,
            'read': message.read,
        })