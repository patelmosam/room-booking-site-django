# room-booking-app (YOYO)

YOYO is a simple hotel room booking site application made with django.

There are two type of user: customer and hotel manager.

both have to first signup and then login.

functionality of hotel manager:
    - manager can signup, login & logout.
    - manager can registor their hotel
    - manager can add room to their hotel
    - manager can see booked rooms by users
    - manager can explore the hotels (not able to book it)

- first manager has to signup by clicking on signup -> manager signup.
- after signup it will redirect to login page to login.
- after login manager has to registor their hotel in my hotel page.
- In my hotel page their are two sections: hotel profile & hotel settings.
- first manager has to set up hotel profile by adding hotel picture (it's not uploading), Name and adderess.
- Then manager has to save setting to hotel like totel no. of rooms, price, type and discription. 
- after saving the profile and settings hotel will be visible on explore page.
- manager also has to add rooms via add room page otherwise rooms will not be available for booking.


functionality of customer:
    - customer can signup, login & logout.
    - customer can explore the hotels. 
    - customer can book hotel rooms.
    - customer can see booking history of their rooms.

- first customer has to signup by clicking on signup -> customer signup.
- after signup it will redirect to login page to login.
- after login customer can explore hotels via explore page.
- In explore page customer can see the hotels card with hotel picture, name, address, price and book option.
- by clicking book button it will redirct to correspnding hotel room booking page.
- In the room booking page customer can book rooms. 
- if room is not availble it will print massage "room is already booked" otherwise "booking sucessfull".
- customer can also view their booking history in history page.

