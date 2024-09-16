# RideBuddy
## About the Project

TThis web app addresses a socio-economic problem in Bangladesh, where I reside. In the capital city, Dhaka, many schools provide a bus service. However, most parents are unable to rely on the city's public transportation system to be safe or timely enough for their children's daily commute to and from school.

The app aims to solve this issue by creating a platform for carpooling among students from the same school who live in the same residential area. This solution not only helps reduce the stress of parents who do not own a car but also offers a safer alternative to public transport. Additionally, it benefits the city by reducing the number of cars on the road, contributing to less traffic and lower emissions.

## Distinctiveness and Complexity

### Subject Matter
This webapp is catered to a specfic issue related to Dhaka city in Bangladesh. It is a uniqe ride sharing app which is different from a social media or e-commerce website. The app utilizes 5 different models other than the Django built-in model for users. Some of the data in these models are auto generated while others are linked with each other.

### Models
The models user are as follows:

1. Locations: This model is to store individual embarcation and disembarcation locations. Their type, as in, whether it is a school or a residential area, as well as other optional directional information about that location. This table is not editable by the common user of the app. It is meant to be edited from the admin module.

2. Trips: this table is to be used as the main storage where all of the rides created by users are stored. All the of relevant trip details are stored here.

3. Spot Bookings: When a trip is booked by other users, it creates a booking in this table which is linked to the trip on a one to many relationship.

4. Messages: When a booking request is made and also when a booking is accepted or rejected an auto generated message is created for informing the relevant party. These messages are stored in the table.

5. FAQ: This table contains questions and answers for the FAQ section. Can be changed from admin module only.

### Front end
In addition to the the backend work, there is some javascript work done for the front-end to create some animations in the home page. bootstrap and javascript is utilized together to create a unique look for other pages. Django template is used for the forms.

Some of the forms do not reload the entire page, instead of form submission, javascript fetch is used to communicate with the server. The number of unread messages is also automatically fetched from the server upon user login through fetch.



### Features
#### Installation
##### Usage
###### Contact
