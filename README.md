# RideBuddy
## About the Project

TThis web app addresses a socio-economic problem in Bangladesh, where I reside. In the capital city, Dhaka, many schools provide a bus service. However, most parents are unable to rely on the city's public transportation system to be safe or timely enough for their children's daily commute to and from school.

The app aims to solve this issue by creating a platform for carpooling among students from the same school who live in the same residential area. This solution not only helps reduce the stress of parents who do not own a car but also offers a safer alternative to public transport. Additionally, it benefits the city by reducing the number of cars on the road, contributing to less traffic and lower emissions.

## Distinctiveness and Complexity

### Distinctive Subject Matter
This webapp is catered to a specfic issue related to Dhaka city in Bangladesh. It is a uniqe ride sharing app which is different from a social media or e-commerce website. The app utilizes 5 different models other than the Django built-in model for users. Some of the data in these models are auto generated while others are linked with each other.

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
In order to open new trips, user needs to go to 'Make Trips' route from the nav bar. in this page, the user can find a button to open a form that will open new trip. In order to do it, they will need to fill this form to populate the following fields: 
1. origin: where does this trip start? this is a dropdown populated from Locations model.
2. destination: where does this trip finish? this is a dropdown populated from Locations model.
3. description_text: Any other information needed to be communicated to the ride partners
4. departure_time: at what time does the departure take place.
5. open_seats: how any seats in the car available initially. 
6. valid_for: trip opener (owner) needs to specify the period for which this trip will be valid. The choices are, Monthly, Quarterly, Semi-Annual, or Annual
7. valid_till: this field is not visible to the user. it is auto populated with a specific based on a calculation that will be made based on what the user has chosen above. 
8. trip_owner: another invisible field which is autopupulated. Will be filled based on who opened the trip. is linked to the user table.




### Creating Trips: 


#### Installation
##### Usage
###### Contact
