# RideBuddy

## About the Project

TThis web app addresses a socio-economic problem in Bangladesh, where I reside. In the capital city, Dhaka, many schools provide a bus service. However, most parents are unable to rely on the city's public transportation system to be safe or timely enough for their children's daily commute to and from school.

The app aims to solve this issue by creating a platform for carpooling among students from the same school who live in the same residential area. This solution not only helps reduce the stress of parents who do not own a car but also offers a safer alternative to public transport. Additionally, it benefits the city by reducing the number of cars on the road, contributing to less traffic and lower emissions.

## Distinctiveness and Complexity

### Distinctive Subject Matter

This webapp is catered to a specfic issue related to Dhaka city in Bangladesh. It is a uniqe ride sharing app which is different from a social media or an e-commerce website. The app utilizes 5 different models other than the Django built-in model for users. Some of the data in these models are auto generated while others are linked with each other.

### Front end

In addition to the Django backend work, there are some javascript work done for the front-end to create some animations in the home page. bootstrap and javascript is utilized together to create a unique look for other pages. Django template is used for the forms.

Some of the forms do not reload the entire page, instead of form submission, javascript fetch is used to communicate with the server. The number of unread messages is also automatically fetched from the server upon user login through fetch.

The webapp is fully mobile responsive. Details of the trips are shown in a card which is generated from a template. The button functions are different based on whether the trip owner is or some other user is viewing it.

### Models

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

Existing trips can be deleted by the owner by clicking the Delete button in the top right corner.

#### Booking a ride:

In order to book a ride, a user needs to click the 'Book a Trip' link from the nav bar. Here, the user will be able to see all currently active trips. 

user also has the option to filter the available trips based on origin and destination locations. The list of trips in the page will dynamically update based on what is chosen the this filter. Selecting none means all will be shown.

After the requesting user finds a suitable trip from the list, they need to send a request for a spot form the form that can be opened from the 'Book a Spot' button. they need to add any details of the request in the comments field with there request and it will be visible for the trip owner's approval window.

confirmation message will be shown once a request is sent successfully.

#### Messeges

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

#### Installation
###### Contact
email: shumittaher@outlook.com
github: shumittaher
linkedin: https://www.linkedin.com/in/shumit-taher-42a96bb5/