# Name: Charlie
# Period: PM
# Disneyland Trip Budget Calculator

# saying hello
print("aloha")
print("Welcome to the Disneyland Trip Budget Calculator")
print("I will ask you for some information about your trip")
print()

# basic trip information
name = input("What is your name? ")
num_people = int(input("How many people are there? "))
days = int(input("How many park days (2-5)? "))
nights = int(input("How many nights in the hotel? "))
print()

park_hopper_price = float(input("How much does the Park Hopper ticket cost per person? "))

# multiply by people for full price
ticket_price = park_hopper_price * num_people

# float() for decimals
food_per_person = float(input("How much will food cost per person per day? "))

# food calculation
food_cost = food_per_person * num_people * days

#extra prints for spacing
souvenir_per_person = float(input("How much will each person spend on souvenirs? "))
souvenir_cost = souvenir_per_person * num_people
print()

# hotel calculations
room_price = float(input("How much does a hotel room cost per night? "))
num_rooms = int(input("How many rooms will you need? "))
hotel_price = room_price * num_rooms * nights
print()

# driving calculations
one_way_distance = float(input("How far is it to Disneyland in miles? "))
round_trip = one_way_distance * 2

mpg = float(input("How many MPG does your vehicle get? "))

# gas calculations
gas_price = float(input("How much does regular gas currently cost per gallon? "))
gallons_needed = round_trip / mpg
gas_cost = gallons_needed * gas_price

# disneyland parking calculations
parking_per_day = float(input("How much does it cost to park per day at Disneyland? "))
disneyland_parking = parking_per_day * days
print()

# final trip calculations
final_cost = ticket_price + food_cost + souvenir_cost + hotel_price + gas_cost + disneyland_parking
per_person = final_cost / num_people
per_day = final_cost / days

trip_budget = float(input("What is your total trip budget? "))
budget_diff = trip_budget - final_cost
print()

# extra variables for easier readibility
total_people = num_people
total_days = days
total_nights = nights
total_miles = round_trip
total_gallons = gallons_needed
total_rooms = num_rooms

print("======================================")
print("       DISNEYLAND TRIP REPORT")
print("======================================")
print(f"Name: {name}")
print(f"Number of people: {total_people}")
print(f"Park days: {total_days}")
print(f"Hotel nights: {total_nights}")
print(f"Number of rooms: {total_rooms}")
print()
print(f"Park Hopper price per person: ${park_hopper_price:,.2f}")
print(f"Total ticket cost: ${ticket_price:,.2f}")
print(f"Total food cost: ${food_cost:,.2f}")
print(f"Total souvenir cost: ${souvenir_cost:,.2f}")
print(f"Total hotel cost: ${hotel_price:,.2f}")
print()
print(f"Round-trip distance: {total_miles:,.2f} miles")
print(f"Vehicle MPG: {mpg:,.2f}")
print(f"Gallons of gas needed: {total_gallons:,.2f}")
print(f"Gas price per gallon: ${gas_price:,.2f}")
print(f"Total gas cost: ${gas_cost:,.2f}")
print(f"Total parking cost: ${disneyland_parking:,.2f}")
print()
print(f"FINAL TRIP COST: ${final_cost:,.2f}")
print(f"Cost per person: ${per_person:,.2f}")
print(f"Cost per park day: ${per_day:,.2f}")
print(f"Trip budget: ${trip_budget:,.2f}")
print(f"Budget difference: ${budget_diff:,.2f}")
print()
print("Thank you for using my Disneyland Trip Budget Calculator")
print("Have a great trip to Disneyland buddy")