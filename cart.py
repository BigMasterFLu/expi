import datetime  # used to put today's date on the receipt

# ---------- STORE INVENTORY ----------
products = {  # product name -> price
    "Air Freshener": 3.50,  # hanging car air freshener
    "Microfiber Towel": 6.00,  # towel for drying and detailing
    "Tire Shine": 9.25,  # spray that makes tires glossy
    "Car Wax": 14.99,  # paste wax to protect the paint
    "Phone Mount": 19.99,  # dashboard phone holder
}

# ---------- CUSTOMER CART ----------
shopping_cart = {}  # product name -> quantity (each product appears once)


def get_number(prompt, low, high, error):  # asks until a number in range is entered
    choice = int(input(prompt))  # first attempt
    while choice < low or choice > high:  # keep asking while out of range
        print(error)  # tell the user what went wrong
        choice = int(input(prompt))  # ask again
    return choice  # hand back the valid number


def get_quantity(name):  # asks until a quantity above 0 is entered
    amount = int(input(f"How many {name} would you like to add? "))  # first attempt
    while amount <= 0:  # quantity must be positive
        print("Quantity must be greater than 0!")  # tell the user what went wrong
        amount = int(input(f"How many {name} would you like to add? "))  # ask again
    return amount  # hand back the valid quantity


def round_money(amount):  # rounds money to cents, halves round up (0.625 -> 0.63)
    return int(amount * 100 + 0.5 + 1e-9) / 100  # shift to cents, round, shift back


def display_products():  # shows the store inventory
    print("\n========== AVAILABLE PRODUCTS ==========\n")  # header
    number = 1  # counter for menu numbers
    for name, price in products.items():  # loop through every product and price
        print(f"{number}. {name:<18} ${price:.2f}")  # number, name, price
        number += 1  # next menu number


def add_product(cart):  # adds a product and quantity to the cart
    display_products()  # show what can be bought
    names = list(products.keys())  # temporary list linking menu numbers to names
    num = get_number("\nEnter product number: ", 1, len(names),
                     f"Invalid product!\nPlease choose a number between 1 and {len(names)}.")  # valid pick
    name = names[num - 1]  # convert menu number to product name
    amount = get_quantity(name)  # how many to add
    if name in cart:  # product already in cart
        cart[name] += amount  # add to its existing quantity
    else:  # product is new to the cart
        cart[name] = amount  # create a new entry
    print(f"\nAdded {amount} {name} to your cart!")  # confirm
    print(f"{name} quantity is now {cart[name]}.")  # show new quantity


def remove_product(cart):  # removes one unit of a product
    if len(cart) == 0:  # nothing to remove
        print("\nYour shopping cart is empty!\nThere is nothing to remove.")  # warn
        return  # back to menu
    print("\n========== YOUR SHOPPING CART ==========\n")  # header
    number = 1  # counter for item numbers
    for name, amount in cart.items():  # list every cart item and quantity
        print(f"{number}. {name} - Quantity: {amount}")  # name and quantity
        number += 1  # next item number
    names = list(cart.keys())  # temporary list linking item numbers to names
    num = get_number("\nEnter item number to remove: ", 1, len(names),
                     "That item does not exist in your cart!")  # valid pick
    name = names[num - 1]  # convert item number to product name
    cart[name] -= 1  # take one unit away
    print(f"\nRemoved 1 {name} from your cart!")  # confirm
    if cart[name] == 0:  # none left
        del cart[name]  # delete the key-value pair
        print(f"{name} is no longer in your cart.")  # tell the user
    else:  # some still left
        print(f"{name} quantity is now {cart[name]}.")  # show new quantity


def calculate_total(cart):  # returns the subtotal
    total = 0  # running total
    for name, amount in cart.items():  # every product and quantity in the cart
        total += products[name] * amount  # price from inventory times quantity
    return total  # subtotal


def count_items(cart):  # returns total items including quantities
    count = 0  # running count
    for amount in cart.values():  # every quantity in the cart
        count += amount  # add it
    return count  # total items


def calculate_discount(subtotal):  # returns the discount rate as a decimal
    if subtotal >= 40:  # $40 or more
        return 0.15  # 15%
    elif subtotal >= 20:  # $20 to under $40
        return 0.10  # 10%
    elif subtotal >= 10:  # $10 to under $20
        return 0.05  # 5%
    else:  # under $10
        return 0  # no discount


def print_items(cart, numbered):  # prints each cart line with price, quantity, line total
    print(f"{'Product':<22}{'Unit Price':>10}{'Quantity':>11}{'Line Total':>13}")  # column labels
    number = 1  # counter for row numbers
    for name, amount in cart.items():  # every product and quantity in the cart
        price = products[name]  # unit price from the inventory dictionary
        label = f"{number}. {name}" if numbered else name  # add number only if asked
        price_text = f"${price:.2f}"  # unit price as text
        line_text = f"${price * amount:.2f}"  # line total as text
        print(f"{label:<22}{price_text:>10}{amount:>11}{line_text:>13}")  # one row
        number += 1  # next row number


def display_cart(cart):  # option 4
    if len(cart) == 0:  # empty cart
        print("\nYour shopping cart is empty!")  # warn
        return  # back to menu
    print("\n========== YOUR SHOPPING CART ==========\n")  # header
    print_items(cart, True)  # every row, numbered
    print(f"\nTotal Items: {count_items(cart)}")  # count including quantities
    print(f"Subtotal: ${calculate_total(cart):.2f}")  # subtotal


def display_total(cart):  # option 5
    print("\n========== CURRENT TOTAL ==========\n")  # header
    print(f"Subtotal: ${calculate_total(cart):.2f}")  # subtotal ($0.00 if empty)


def checkout(cart):  # option 6, returns True if checkout finished
    if len(cart) == 0:  # can't check out with nothing
        print("\nYour shopping cart is empty! Add something before checking out.")  # warn
        return False  # stay in the program
    subtotal = calculate_total(cart)  # cart subtotal
    rate = calculate_discount(subtotal)  # discount rate
    saved = subtotal * rate  # money saved
    final = subtotal - saved  # amount owed
    today = datetime.date.today().strftime("%m/%d/%Y")  # today's date as MM/DD/YYYY
    print("\n========== RECEIPT ==========")  # header
    print(f"Date: {today}\n")  # date line
    print_items(cart, False)  # every row, unnumbered
    print(f"\nTotal Items:    {count_items(cart)}")  # count including quantities
    print(f"Subtotal:       ${subtotal:.2f}")  # subtotal
    print(f"Discount:       {round(rate * 100)}%")  # discount percent
    print(f"Amount Saved:   ${round_money(saved):.2f}")  # savings
    print(f"Final Total:    ${round_money(final):.2f}")  # final amount
    print("\nThank you for shopping!")  # goodbye
    return True  # checkout done


def show_menu():  # prints the main menu
    print("\n========== SMART SHOPPING CART ==========\n")  # header
    print("1. View Available Products")  # option 1
    print("2. Add Product to Cart")  # option 2
    print("3. Remove Product from Cart")  # option 3
    print("4. View Shopping Cart")  # option 4
    print("5. View Current Total")  # option 5
    print("6. Checkout\n")  # option 6


# ---------- MAIN PROGRAM ----------
done = False  # becomes True after checkout
while not done:  # repeat the menu until checkout
    show_menu()  # display options
    choice = get_number("Enter your choice: ", 1, 6, "Invalid option!")  # valid menu pick
    if choice == 1:  # view products
        display_products()  # show inventory
    elif choice == 2:  # add product
        add_product(shopping_cart)  # add with quantity
    elif choice == 3:  # remove product
        remove_product(shopping_cart)  # remove one unit
    elif choice == 4:  # view cart
        display_cart(shopping_cart)  # show cart details
    elif choice == 5:  # view total
        display_total(shopping_cart)  # show subtotal
    else:  # checkout
        done = checkout(shopping_cart)  # ends loop only if checkout succeeded
