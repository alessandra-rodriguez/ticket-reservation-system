# Railroad Reservation System

## Description
This application interacts with a SQLite database to manage train passenger info and ticket bookings. Users may perform queries to check tickets, train capacities, and delete tickets using a Tkinter GUI.

## Features
* Check Tickets by name, date, or are: Retrieve passenger information based on the first name and last name, a specific departure date or age range and view their details.
* Check Train Capacity: Display the number of passengers booked on each train.
* Check Train Passengers: Retrieve the list of passengers booked on a specific train.
* Delete Tickets by Name & Train: Delete booked tickets based on passenger name and train name.
* Clear Output: Clear the displayed query results.

## Usage
1. Clone this repo locally
2. Install and update relevant libraries
3. Initialize the SQLite database using the terminal command:
sqlite3 train.db < rrs.sql
4. Enter passenger information or query details in the provided text boxes.
5. Click the corresponding button to perform the desired query.
6. View the results displayed in a pop-up window.
7. Use the "Clear Output" button to remove previous query results
