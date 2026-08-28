# Name: Charlie
# Period: PM
# Disneyland Trip Budget Calculator

print("aloha")
print("Welcome to disney trip calculator")
print("Will ask for some information")
name = input("What is your name?")
num_people = int(input("How many people are there?"))
days = int(input("How many park days(2-5)?"))
nights = int(input("How many nights in the hotel?"))
print()
ticket_price = float(input("How much does the Park Hopper price cost?")) * num_people
food_cost = float(input("How much does it cost for food per person?")) * num_people
souviner_cost = float(input("How much does it cost for souviners per person?")) * num_people
print()
hotel_price = float(input("How much does it cost per room per night?")) * float(input("How many rooms?"))
print()
round_trip = 2* int(input("How far is it to disneyland?"))
mpg = int(input("How much mpg does your vehicle have?"))
gas = float(input("How much does gas currently cost?"))
gallons_needed = round_trip / mpg
gas_cost = gallons_needed * gas
disneyland_parking = int(input("how much does it cost to park per day at disneyland")) * days
print()
final_cost = ticket_price + food_cost + souviner_cost + hotel_price + gas_cost + disneyland_parking
per_person = final_cost / num_people
per_day = final_cost / days
budget = float(input("What is your budget?"))
budget_diff = budget-final_cost
print()
