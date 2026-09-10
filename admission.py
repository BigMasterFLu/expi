# Name: Charlie
# Period: PM
# Theme Park Admission & Ride Eligibility System

# say hi to the guest and hype up the park
print("Welcome to Midnight Adventure Park!")
print("Let's get your ticket and park information ready.")
print("This program will calculate your admission price and ride eligibility.")
print()


# grab all the guest's deets
guest_name = input("What is your name? ")
age = int(input("How old are you? "))
height = float(input("How tall are you in inches? "))
ticket_type = input("What ticket did you purchase? regular/premium: ")
park_member = input("Are you a park member? yes/no: ")
visiting_with_adult = input("Are you visiting with an adult? yes/no: ")
visit_time = input("Are you visiting during the morning or evening? ")
print()


# figure out the base ticket price from how old they are
def calculate_admission(age):
    if age <= 4:
        price = 0
    elif age <= 12:
        price = 15
    elif age <= 64:
        price = 30
    else:
        price = 20

    return price


# knock money off based on membership + when they're rolling through
def calculate_discount(price, member, visit_time):
    # members pulling up in the evening get the biggest bag off the price
    if member == "yes" and visit_time == "evening":
        final_price = price - 10
    elif member == "yes":
        final_price = price - 5
    elif visit_time == "evening":
        final_price = price - 3
    else:
        final_price = price

    # no way we're paying them, clamp it so it doesn't go negative
    if final_price < 0:
        final_price = 0

    return final_price


# see how crazy of a ride they're allowed on
def ride_level(age, height):
    # check the craziest ride first and work our way down
    if age >= 16 and height >= 54:
        level = "Extreme Rides"
    elif age >= 12 and height >= 48:
        level = "Thrill Rides"
    elif age >= 8 and height >= 42:
        level = "Family Rides"
    elif height >= 36:
        level = "Kiddie Rides"
    else:
        level = "No Rides"

    return level


# do they need a grown-up babysitting them or nah
def check_supervision(age, visiting_with_adult):
    # anyone under 13 rolling solo is a no-go
    if age < 13 and visiting_with_adult == "no":
        status = "Adult Required"
    else:
        status = "Approved"

    return status


# extra credit: check if this guest is built different (vip)
def check_vip(ticket_type, park_member, age):
    # premium members or premium seniors get the vip treatment
    if ticket_type == "premium" and park_member == "yes" or age >= 65 and ticket_type == "premium":
        access = "VIP ACCESS"
    else:
        access = "STANDARD ACCESS"

    return access


# run all the functions and stash what they spit back
admission_price = calculate_admission(age)
final_admission_price = calculate_discount(admission_price, park_member, visit_time)
guest_ride_level = ride_level(age, height)
supervision_status = check_supervision(age, visiting_with_adult)
vip_status = check_vip(ticket_type, park_member, age)


# peep whether they splurged on the premium ticket
if ticket_type == "premium":
    premium_message = "PREMIUM BONUS: Free snack and priority ride access!"
else:
    premium_message = "Regular Ticket: Standard park access."


# dump the whole guest report to the screen
print("========================================")
print("        MIDNIGHT ADVENTURE PARK")
print("              GUEST REPORT")
print("========================================")
print()

print("Guest:", guest_name)
print("Age:", age)
print("Height:", height, "inches")
print("Ticket Type:", ticket_type)
print("Park Member:", park_member)
print("Visit Time:", visit_time)
print()

print("Regular Admission: $", admission_price)
print("Final Admission: $", final_admission_price)
print()

print("Highest Ride Level:")
print(guest_ride_level)
print()

print("Supervision Status:")
print(supervision_status)
print()

print("Premium Ticket Status:")
print(premium_message)
print()

print("VIP Status:")
print(vip_status)
print()


# hit the guest with a lil personalized send-off
if supervision_status == "Adult Required":
    print(guest_name + ", you need an adult with you before entering the park.")
elif guest_ride_level == "Extreme Rides":
    print(guest_name + ", you're cleared for our most extreme rides!")
elif guest_ride_level == "No Rides":
    print(guest_name + ", enjoy the shows, food, and other park attractions!")
elif age <= 4 or age >= 65:
    print(guest_name + ", we hope you have an amazing day at the park!")
elif ticket_type == "premium":
    print(guest_name + ", enjoy your premium benefits and priority ride access!")
else:
    print(guest_name + ", have an awesome day exploring the park!")

print()
print("========================================")
print("Thanks for visiting Midnight Adventure Park!")
print("========================================")
