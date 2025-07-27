#Individual Coursework-DOC333 (Flight Reservation System )
#Intializing Variables
#I used a combination of If/else and def tag to make the code work smoother

Username=""
Password=""
q1=""
#q-question
Business=3
Economy=5

flights=[]
customers=[]
availables=[]
bookings=[]
view_booking=[]

stafflogintitle1="CloudFare Airlines"
stafflogintitle2="Staff Login"
Mainmenutitle1="CloudFare Airlines"
Mainmenutitle2="Main Menu"
correct_username2025 = "sanithu"
correct_password2025 = "20250212"


#Separate the menu from the rest 
line = "-"*80
print(line)

#Figure 1
print(stafflogintitle1.center(80))
print(stafflogintitle2.center(80))


#Tracking User inputs (Username and Password)
Username=str(input("Username -")).replace(" ", "")
Password=str(input("Password -")).replace(" ", "")
if Username == correct_username2025 and Password == correct_password2025:
     def login():
          q1 = input("Do you want to login (Yes/No)? ").lower()
          if q1 == "yes":
               print("Login successful.")
               return True
          elif q1 == "no":
               return False
          else:
               print("Invalid input. Please type Yes or No.")
               return False
else:
     print("Invalid input")
     import sys
     sys.exit()
#defining addflight as a dictonary for figure 3
#(Aussumption - 2)This and the defining below presumes the user enters the flight no correctly.
def addflight():
    print(line)
    print("CloudFare Airlines".center(80))
    print("Add Flight Details".center(80))

    while True:
        flight_no = input("1) Flight No - ").upper()
        #Must be like JFK###
        if flight_no.startswith("JFK") and len(flight_no) == 6 and flight_no[3:].isdigit():
            break
        else:
            print("Invalid flight number. Must start with JFK and be followed by 3 digits.")
    print("2) Departure (From) - JFK")
    departure = "JFK"
    valid_arrivals = ["Orlando", "Miami", "Los Angeles"]
    while True:
        arrival = input("3) Arrival (To) - ").title()
        if arrival in valid_arrivals:
            break
        else:
            print("Invalid destination. Choose from: Orlando, Miami, Los Angeles.")
    departure_date = input("4) Departure Date - ")
    departure_time = input("5) Departure Time - ")
    print("6) Total no of economy class seats - 5")
    economy_seats = 5

    print("7) Total no of business class seats - 3")
    business_seats = 3

    print("8) Fare for an economy class person - 500")
    economy_fare = 500

    print("9) Fare for a business class person - 1000")
    business_fare = 1000
    flight = {
        "flight_no": flight_no,
        "departure": departure,
        "arrival": arrival,
        "departure_date": departure_date,
        "departure_time": departure_time,
        "economy_seats": economy_seats,
        "business_seats": business_seats,
        "economy_fare": economy_fare,
        "business_fare": business_fare
    }
    confirm = input("Do you want to add this flight? (Yes/No): ").lower()
    if confirm == "yes":
        flights.append(flight)
        print("Flight added successfully.")
    else:
        print("Flight not added.")
    


#defining registercustomer as a dictonary for figure 4
def registercustomer():
    print(line)
    print("CloudFare Airlines".center(80))
    print("Register Customer".center(80))

    customer_id = input("1)Customer ID-").replace(" ", "")
    #Input here must be capital
    if not (customer_id.startswith("C") and len(customer_id) == 4 and customer_id[1:].isdigit()):
        print("Invalid Customer ID. It must start with C and be followed by 3 digits.")
        return
     
    customer={"customer_id":(customer_id),
              "customer_name":input("2)Name-"),
              "passport_number":input("3)Passport Number-"),
              "customer_address":input("4)Adress-"),
              "telephone_number":input("5)Telephone Number-")}
    customer_confirm = input ("Do you want to save (Yes/No)?").lower()
    if customer_confirm == "yes":
        customers.append(customer)
        print("Customer registered.")
    else:
        print("Customer not registered.")

#Figue 5 work and defining a dictonary for figure 5
import random

def generate_flight_id():
    number = random.randint(1, 999)
    return f"JFK{number:03}"

def available_fli():
    global Business, Economy
    line = "-" * 80
    print(line)
    print("CloudFare Airlines".center(80))
    print("Search for Available Flights".center(80))

    available_confirm = input("Do you want to search (Yes/No)? ").lower()
    if available_confirm != "yes":
        print("Flight not searched.")
        return

    date = input("1) Departure Date - ")
    time = input("2) Departure Time (6:30 am/2:00 pm/8:30 pm) - ").lower()
    origin = input("3) Flying From - JFK ")

    #Destination 
    dest_code = input("4) Flying To (ORL/MIA/LAX) - ").upper()
    dest_map = {"ORL": "Orlando", "MIA": "Miami", "LAX": "Los Angeles"}
    dest = dest_map.get(dest_code, None)

    scheduled_flights = [
        ("6:30 am", "Orlando"),
        ("2:00 pm", "Miami"),
        ("8:30 pm", "Los Angeles")
    ]

    if dest and (time, dest) in scheduled_flights:
        flight_no1 = generate_flight_id()
    else:
        print("Invalid departure time or destination for scheduled flights.")
        flight_no1 = "Invalid"

    print(f"5) Flight No - {flight_no1}")

    travel_class = input("6) Travel Class (Business/Economy)- ").capitalize()

    if travel_class == "Business":
        if Business > 0:
            Business -= 1
            seats_available = Business
        else:
            seats_available = 0

    elif travel_class == "Economy":
        if Economy > 0:
            Economy -= 1
            seats_available = Economy
        else:
            seats_available = 0

    else:
        print("Invalid option. Please select Business or Economy.")
        return

    print(f"7) No of seats available in the flight - {seats_available}")

    available = {
        "Departure Date": date,
        "Departure Time": time,
        "From": origin,
        "To": dest,
        "Flight No": flight_no1,
        "Class": travel_class,
        "Seats Available": seats_available
    }

    print(line)

#Defining a dictonary figure 6
def booking_a_flight():
    print(line)
    print("CloudFare Airlines".center(80))
    print("Booking a flight".center(80))

    # Tracking user inputs
    flight_booking_no = input("1) Flight No - ")
    customer_name_booking = input("2) Customer Name - ")
    passport_number_booking = input("3) Passport Number - ")
    destination_airport_booking = input("4) Destination Airport (Orlando/Miami/Los Angeles) - ").title().replace(" ", "")

    
    if destination_airport_booking == "Orlando":
        departure_time_booking = "6.30 am"
    elif destination_airport_booking == "Miami":
        departure_time_booking = "2.00 pm"
    elif destination_airport_booking == "Los Angeles":
        departure_time_booking = "8.30 pm"
    else:
        print("Invalid destination. Booking cancelled.")
        return

   
    departure_date_booking = input("5) Departure Date - ")
    print("6) Departure Time:", departure_time_booking) 
  
    travel_class_booking = input("7) Travel Class (Business Class/Economy Class) - ")

    #Figure 6 dictionary
    booking = {
        "flight_booking_no": flight_booking_no,
        "customer_name_booking": customer_name_booking,
        "passport_number_booking": passport_number_booking,
        "destination_airport_booking": destination_airport_booking,
        "departure_date_booking": departure_date_booking,
        "departure_time_booking": departure_time_booking,
        "travel_class_booking": travel_class_booking
    }

    
    booking_confirm = input("Do you want to book (Yes/No)? ").lower()
    if booking_confirm == "yes":
        bookings.append(booking)
        print("Flight booked.")
    else:
        print("Flight not booked.")


             
#Defining a dictonary figure 7
def view_booking_deal():
    line = "-" * 80
    print(line)
    print("CloudFare Airlines".center(80))
    print("View booking details".center(80))

    departure_date = input("Enter Departure Date: ")
    print("\n" + " " * 5 + "Departure Date", ":", departure_date)
    print()

    view_booking_confirm = input("Do you want to view the bookings? (Yes/No): ").lower()

    if view_booking_confirm == "yes":
        print()
        print(" " * 5 + "{:<12}{:<17}{:<15}{:<}".format("Flight No", "Departure Time", "Destination", "No of passengers"))

        found = False
        for booking in bookings:
            if booking["departure_date_booking"] == departure_date:
                print(" " * 5 + "{:<12}{:<17}{:<15}{:<}".format(
                    booking["flight_booking_no"],
                    booking["departure_time_booking"],
                    booking["destination_airport_booking"],
                    booking["customer_name_booking"]
                ))
                found = True

        if not found:
            print(" " * 5 + "No bookings found for this date.")


        print("\nBooking details viewed.")

    else:
        print("\nReturning to main menu...")
            
        
#(Assumption - 1)This is assuming the person entering the data does so with correct capitalization
#Figure 2
if login():
    print(line)
    #Main Menu
    print(Mainmenutitle1.center(80))
    print(Mainmenutitle2.center(80))

    while True:
        print("(1) Add flight details")
        print("(2) Register a customer")
        print("(3) Search for available flight details")
        print("(4) Booking a flight")
        print("(5) View booking details")
        print("(6) Exit")
        choice = input("Your Choice: ").strip()
        if choice=="1":
            addflight()
            
        elif choice=="2":
            registercustomer()
            
        elif choice=="3":
            available_fli()
            
        elif choice=="4":
             booking_a_flight()
        elif choice=="5":
             view_booking_deal()
        elif choice=="6":
            exit()
            break
        else:
            print ("Invalid Input. Please pick an option from 1 to 6.")
else:
    print("Login cancelled.")    


