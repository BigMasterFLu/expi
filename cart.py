import datetime  # used to put today's date on the receipt

# ---------- STORE INVENTORY ----------
products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]  # product names
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]  # prices, same index as products

# ---------- CUSTOMER CART ----------
shopping_cart = []  # each product appears once
quantities = []  # how many of each product, same index as shopping_cart


def get_number(prompt, low, high, error):  # asks until a number in range is entered
    choice = int(input(prompt))  # first attempt
    while choice < low or choice > high:  # keep asking while out of range
        print(error)  # tell the user what went wrong
        choice = int(input(prompt))  # ask again
    return choice  # hand back the valid number


def get_price(name):  # finds the store price of a product
    return prices[products.index(name)]  # matching index in the prices list


def display_products():  # shows the store inventory
    print("\n========== AVAILABLE PRODUCTS ==========\n")  # header
    for i in range(len(products)):  # loop through every product
        print(f"{i + 1}. {products[i]:<10} ${prices[i]:.2f}")  # number, name, price


def add_product(cart, qty):  # adds one product to the cart
    display_products()  # show what can be bought
    num = get_number("\nEnter product number: ", 1, len(products),
                     "Invalid product!\nPlease choose a number between 1 and 6.")  # valid pick
    name = products[num - 1]  # convert menu number to list index
    if name in cart:  # product already in cart
        pos = cart.index(name)  # find where it is
        qty[pos] += 1  # bump its quantity
        print(f"\n{name} quantity increased to {qty[pos]}!")  # confirm
    else:  # product is new to the cart
        cart.append(name)  # add the name
        qty.append(1)  # start its quantity at 1
        print(f"\n{name} was added to your cart!")  # confirm


def remove_product(cart, qty):  # removes one unit of a product
    if len(cart) == 0:  # nothing to remove
        print("\nYour shopping cart is empty!\nThere is nothing to remove.")  # warn
        return  # back to menu
    print("\n========== YOUR SHOPPING CART ==========\n")  # header
    for i in range(len(cart)):  # list every cart item
        print(f"{i + 1}. {cart[i]} - Quantity: {qty[i]}")  # name and quantity
    num = get_number("\nEnter item number: ", 1, len(cart),
                     "That item does not exist in your cart!")  # valid pick
    pos = num - 1  # convert to index
    name = cart[pos]  # remember the name for messages
    if qty[pos] > 1:  # more than one left
        qty[pos] -= 1  # take one away
        print(f"\nOne {name} was removed!\n{name} quantity is now {qty[pos]}.")  # confirm
    else:  # last one
        cart.pop(pos)  # remove name
        qty.pop(pos)  # remove matching quantity so lists stay in sync
        print(f"\n{name} was removed from your cart!")  # confirm


def calculate_total(cart, qty):  # returns the subtotal
    total = 0  # running total
    for i in range(len(cart)):  # every product in the cart
        total += get_price(cart[i]) * qty[i]  # price times quantity
    return total  # subtotal


def calculate_discount(subtotal):  # returns the discount rate as a decimal
    if subtotal >= 40:  # $40 or more
        return 0.15  # 15%
    elif subtotal >= 20:  # $20 to under $40
        return 0.10  # 10%
    elif subtotal >= 10:  # $10 to under $20
        return 0.05  # 5%
    else:  # under $10
        return 0  # no discount


def print_items(cart, qty):  # prints each cart line with quantity and line total
    for i in range(len(cart)):  # every product in the cart
        price = get_price(cart[i])  # store price
        print(f"{i + 1}. {cart[i]:<10} ${price:<8.2f} {qty[i]:<6} ${price * qty[i]:.2f}")  # one row


def display_cart(cart, qty):  # option 4
    if len(cart) == 0:  # empty cart
        print("\nYour shopping cart is empty!")  # warn
        return  # back to menu
    print("\n========== YOUR SHOPPING CART ==========\n")  # header
    print(f"{'Product':<13} {'Price':<9} {'Qty':<6} Total\n")  # column labels
    print_items(cart, qty)  # every row
    print(f"\nTotal Items: {sum(qty)}")  # count including quantities
    print(f"Subtotal: ${calculate_total(cart, qty):.2f}")  # subtotal


def display_total(cart, qty):  # option 5
    if len(cart) == 0:  # empty cart
        print("\nYour shopping cart is empty!")  # warn
        return  # back to menu
    print("\n========== CURRENT TOTAL ==========\n")  # header
    print_items(cart, qty)  # every row
    print(f"\nSubtotal:   ${calculate_total(cart, qty):.2f}")  # subtotal


def checkout(cart, qty):  # option 6, returns True if checkout finished
    if len(cart) == 0:  # can't check out with nothing
        print("\nYour shopping cart is empty! Add something before checking out.")  # warn
        return False  # stay in the program
    subtotal = calculate_total(cart, qty)  # cart subtotal
    rate = calculate_discount(subtotal)  # discount rate
    saved = subtotal * rate  # money saved
    final = subtotal - saved  # amount owed
    today = datetime.date.today().strftime("%m/%d/%Y")  # today's date as MM/DD/YYYY
    print("\n========== RECEIPT ==========\n")  # header
    print(f"Date: {today}\n")  # date line
    print_items(cart, qty)  # every row
    print(f"\nSubtotal:       ${subtotal:.2f}")  # subtotal
    print(f"Discount:       {int(rate * 100)}%")  # discount percent
    print(f"Amount Saved:   ${saved:.2f}")  # savings
    print(f"\nFinal Total:    ${final:.2f}")  # final amount
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
        display_products()
    elif choice == 2:  # add product
        add_product(shopping_cart, quantities)
    elif choice == 3:  # remove product
        remove_product(shopping_cart, quantities)
    elif choice == 4:  # view cart
        display_cart(shopping_cart, quantities)
    elif choice == 5:  # view total
        display_total(shopping_cart, quantities)
    else:  # checkout
        done = checkout(shopping_cart, quantities)  # ends loop only if checkout succeeded
