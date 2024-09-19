# RideBuddy

## About the Project

This web app addresses a socio-economic problem in Bangladesh, where I reside. In the capital city, Dhaka, many schools provide a bus service. However, most parents are unable to rely on the city's public transportation system to be safe or timely enough for their children's daily commute to and from school.

The app aims to solve this issue by creating a platform for carpooling among students from the same school who live in the same residential area. This solution not only helps reduce the stress of parents who do not own a car but also offers a safer alternative to public transport. Additionally, it benefits the city by reducing the number of cars on the road, contributing to less traffic and lower emissions.

## Distinctiveness and Complexity

### Subject Matter

This webapp has been created as the capstone project of CS50W which is run by HarvardX and as per the project instruction is not a social media or an e-commerce site. This is catered to a specfic issue related to Dhaka city in Bangladesh. It is a unique ride sharing app geared towards school goers in Dhaka. 

### Front end

There are some javascript work done for the front-end to create some animations in the home page. bootstrap and javascript is utilized together to create a unique look for other pages. Django template is used for the forms to acheive similar look. 

the Index page has a different look for the navbar if scroll position is on top of the page. this is used to make the navbar see through so that that mask underneath containing a curved line is visible. If user scrolls down, the navbar changes size and becomes visible. on small screen , the navbar collapses inside a burger button.

The big button to create new trips in the 'Make Trips' page has an animation to open and close the form.

Some of the forms do not reload the entire page, instead of form submission, javascript fetch is used to communicate with the server. The number of unread messages is also automatically fetched from the server upon user login through fetch.

The webapp is fully mobile responsive. Details of the trips are shown in a card which is generated from a template. The button functions are different based on whether the trip owner is or some other user is viewing it.

When a user logs in, the number of his unread message are shown in a badge next to him username in the navbar provided it is more than zero.

The trips that are opened, from a trip owners perspective and from a booking requesters perspective are shown using the same template. however, the button appears different based on the context from where it is accessed. when trip owner sees it, the button is for approving booking requests. Versus, when the booking requester user sees it, the button is for sending a booking request. 

When these buttons are clicked they send a fetch request to populate the placeholder below in the collapsed area. The button sends the fetch request to different routes based on the circumstances. this is explained further in the explanation of the routes below.

There are multiple different fetch queries running accross the app. All of them requires a CSRF token to communicate with the django server. In order to do this, in the 'layout.html' (which runs accross every page of the app) the csrf token is saved in a const called csrf. This is then used by all fetch queries.

### Back end 

The app has 7 different routes for pages in the urls.py. There are also 7 different fetch routes. 2 of them have path parameters. 

2 of the pages included required user to be logged in. There pages are for checking messages and making trips. if user is not logged in and clicks on these routes, they will be re-routed to login page as without a user id, these actions cannot be completed.

#### Page generating URLS:

##### login, logout, and register:
The login, logout, and register views are for login, logout and register actions respectively. registering creates an account in user model.

##### index:
The 'index' view is the homepage of the app which will be visible then user opens the site and also in some cases user will be rerouted here. This page contains multiple sections. Django uses a template called index.html to render this. within this template, other sub-templates are loaded from component snippets sub folder in the templates folder. The FAQ section contains data from a model.

##### mypage:
the 'mypage' view is the page where the user can see messages pertaining to them. Django Paginator was used in order to create pages messages. There are 10 messages shown in each page. since there are two sides in the messages page for read and unread messages, these are filtered seperately in the view and sent to the front end. Another context called active_side is sent to communicate which side should be showed by default. This page requires users to be logged in

##### make_trip:
This is the page mainly to be used by trip creators. New trips creation and editting of existing pages will be done from here. Hence, this page also requires user to be logged in. 

In this view, Django send the 'make_trip.html' template to the browser. the context includes the trip making form as well as the active trips fetched from the relevant model for the active user. 

The form interface within the page is first rendered from Template: "form_snippets/form.html". this template is used in multiple other places to make most forms look similar within the app.

Active trips are determined by comparing present date against the date and duration of the trip when it was opened. timezone from django.utils is used to determine present date. timezone for all dates in the app is UTC. localization has not been implemented.

##### find_trip:
This will generate the page from which the user will find the correct trip and send booking request. Django sends the 'find_trip.html' template to the browser. In this template the placeholder for the trips' list remains empty. This is filled seperately agains a HTTP request.

As context, only the search form is sent in this stage which is rendered through "form_snippets/form.html" to make the look similar to other forms.

#### Fetch query routes
##### give_trips:

This route receives GET requests and responds rendered trips as JSON. Here multiple parameters are considered before the response is rendered. various sides of the app utilizes with route to fetch different lists of trips which are populated in the browser. 

the get requests body can contain multiple different parameters as: info_only, booking_trips, trip_id, spec_booking, 

info_only is a boolean used to render the response in two different looks. the looks are taken from 'component_snippets/trips_list.html' or 'component_snippets/trips_list_info.html' based on the boolean value. the messages side uses the trips_list_info.html containing approval status

booking_trips is another boolean value which determines whether the rendered trips will be shown on trip owners' side or booking requester's side. based on this, buttons' will look and function differently. both will generate from 'trips_list.html'

trip_id will give the server a specific trips id. having a value here means the response will only contain one trip as a response.

if specific trip id is not given, the view generates a list of trips, this is filtered based on origin_area, destination_area and active status and rendered list is sent as a response. default status for origin area and destination area is to select all and active only is set as true.

In all cases the list goes through a function in utils.py called addremaining_spots in order to add the number of currently remaining spots in the trip. this is done becuase the opening number of seats is recorded in the Trips model while the number of approved bookings against that trip is recorded in the Spot_Bookings model. Hence calculation is required to figure out the current numeber of remaining spots.

Going through the function number of remaining spots against each trip is included in a dict and together, all such trips and there remaining spots is placed in a list which is then sent to the front end as the context. 

spec_booking refers to a specific booking request id which at this stage is forwarded directly to the client side to populate a data attibute. This becomes relevant at a later stage as follows: 

The trips list is shown as boxes for each trip in the front end. the boxes contain collapsable section which is initially populated by a placeholder called from 'load_box.html'. depending on whether this box is being shown to the trip owner or booking requester, this placeholder is replaced by either a subform containing all the booking request received against the trip so far or by a form to request for a booking. this is done through another fetch which runs when the collapsed section is opened. spec_booking is sent in this context to later inform that fetch whether to fetch a single booking request or a list of all booking requests. 

##### give_bookingreq_forms:

This route supplies a form through a user can send a booking request for a specific trip. This form gets prepopulated with user id who is logged in and trip id which can be extracted by checking from which trip box this request was send. the pre-population of this data happens through a function in utils.py called make_booking_form. 

The form has a dropdown field to specify how many sits are to be requested. The form is created dynamically to only include options up to the number of sits that are available.

##### give_bookingreqs_list:

This route supplies the list of booking requests. This gets populated in the trips' box when the trip owners open them. This also supplies either list of all booking requests against a trip or a specific booking request depending on the fetch query mentioning a 'spec_booking'. The reason for this is, when the trip owner is trying to access this from the messages window, we wanted to only show the specific booking request against which the message was generated.

The list is rendered from template 'bookingreq_list.html' and send as a json response.

##### booking_request:

This route records new booking requests and updates the model against a POST request or alternatively can update status of approval of an existing booking request against a PUT. It also generates a message in the Message model. Content of the message depends on the POST or PUT request. The messege sending is done through send_message function in utils.py.

When the booking request is created, in the model the apporval status is kept as false. It is stored in a boolean field. If it is approved, the boolean field is updated to be true. If the request is declined through the PUT, the booking req is deleted all together from the model.

When approving, it is checked whether sufficient number of seats are available in the trip first. this is done through calling the find_remaining_spots from utils.

When booking request is successful, approved or rejected or cannot be approved due to insufficient seats, the jason response contains that information for update in the frontend.

##### give_unread: 

This route provides the number of unread messages from the Messages model for the logged in user to be showed in a badge against the user name that appears in the navbar. this fetch is autogenerated when user logs in and the username is displayed. if number of unread messages is more than 99 then the route will simple return '99+'.

##### messages_put:

This route can be used to change the status of the message from 'unread' to 'read'.

##### delete_trip: 

this route receives a PUT request and deletes a trip as per the trip number given in the request body.

### Models

The app utilizes 5 different models other than the Django built-in model for users. Some of the data in these models are auto generated while others are linked with each other.

The models user are as follows:

1. Locations: This model is to store individual embarcation and disembarcation locations. Their type, as in, whether it is a school or a residential area, as well as other optional directional information about that location. This table is not editable by the common user of the app. It is meant to be edited from the admin module.

2. Trips: this table is to be used as the main storage where all of the rides created by users are stored. All the of relevant trip details are stored here.

3. Spot Bookings: When a trip is booked by other users, it creates a booking in this table which is linked to the trip on a one to many relationship.

4. Messages: When a booking request is made and also when a booking is accepted or rejected an auto generated message is created for informing the relevant party. These messages are stored in the table.

5. FAQ: This table contains questions and answers for the FAQ section. Can be changed from admin module only.

## Features

### Opening new trips and editing existing

#### Creating Trips: 

In order to open new trips, user needs to go to 'Make Trips' route from the nav bar. in this page, the user can find a button to open a form that will open new trip. In order to do it, they will need to fill this form to populate the following fields: 

1. origin: where does this trip start? this is a dropdown populated from Locations model.

2. destination: where does this trip finish? this is a dropdown populated from Locations model.

3. description_text: Any other information needed to be communicated to the ride partners

4. departure_time: at what time does the departure take place.

5. open_seats: how any seats in the car available initially. 

6. valid_for: trip opener (owner) needs to specify the period for which this trip will be valid. The choices are, Monthly, Quarterly, Semi-Annual, or Annual

7. valid_till: this field is not visible to the user. it is auto populated with a specific based on a calculation that will be made based on what the user has chosen above. 

8. trip_owner: another invisible field which is autopupulated. Will be filled based on who opened the trip. is linked to the user table.

when user clicks the save button upon filling up this form, a new trip is opened.

#### Editing Existing Trips:

Once a trip is opened, it will show up in the same window. ie. the users can see all of their owned trips under the 'make trips' link. from here, they can also see, the requests to join each trips by clicking 'Requests' button. This will fetch a list of all the booking requests recieved against the trip from the server.

trip owners have the option to approve or reject each request based on their own judgement and information given by the requester in the 'Message' column. This column only shows the starting of the message but the full message can be opened in a modal by clicking on the request's row in the table.

Once the booking request is Approved or Rejected (confirmation required through a modal), the row showing the booking request will change color to show the changed status as well as the number of open seats will change.

Existing trips can be deleted by the owner by clicking the Delete button that appears when they mouse over the trip in this window.

### Booking a ride

In order to book a ride, a user needs to click the 'Book a Trip' link from the nav bar. Here, the user will be able to see all currently active trips. 

user also has the option to filter the available trips based on origin and destination locations. The list of trips in the page will dynamically update based on what is chosen the this filter. Selecting none means all will be shown.

After the requesting user finds a suitable trip from the list, they need to send a request for a spot form the form that can be opened from the 'Book a Spot' button. they need to add any details of the request in the comments field with there request and it will be visible for the trip owner's approval window.

confirmation message will be shown once a request is sent successfully.

### Messeges

At the moment, the system does not have any chat system between users. Hence, all messages are system generated. 

There are following types of system generated messages in the system:

1. To Trip Owners:
    * New Request for booking

2. To booking reqeusters:
    * Request Approved
    * Request Denied / Deleted 

These self explanatory messages are viewable by clicking the username (if user is logged in) in the navbar's right side. The username in the navbar will have a badge contianing number of unread messages (between 1 to 9 and 9+). Clicking the link takes the user to the messages page. 

In the messages page, the messages will be shown under two tabs, one is for read messages and another for unread messages. clicking on the message will open a modal. content on the modal will be depending on the what type of message it is. 

In case, it is a new request, the modal will contain the request approval window and the user will have the option to approve or reject it from there. On the other hand, if the message contains info to booking requsters about approval or rejection, the modal will contain further details of exactly which trip's booking request it was.

Once a message is opened, it will change color to indicate it was read and backend database will be updated. The next time the user visits this page, the message will appear in the 'read' side tab.

This link has pagination implemented and messages are shown 10 per page only.

### Installation and setup

This is a Django app with no other installations of python packages. It utilizes online resources such as bootstrap cdn, a fontawesome kit for icons and google fonts.

Admin id is created with username 'Admin' and password 'Admin' for testing and demo purposes. '/admin' route gives access to the admin module. users are free to create accounts from register route and use the app as required.

app can be run in debug mode from terminal by command: 'python3 manage.py runserver' or 'python manage.py runserver' depeneding on the python version in the system.

## Contact

For more information or any inquiries, feel free to reach out:

- **Email**:    [shumittaher@outlook.com](mailto:shumittaher@outlook.com)
- **GitHub**:   [shumittaher](https://github.com/shumittaher)
- **LinkedIn**: [Shumit Taher](https://www.linkedin.com/in/shumit-taher-42a96bb5/)
