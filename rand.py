import random  # lets me make random numbers

num = random.randint(1, 10)  # picks a random number from 1 to 10
previous_guesses = []  # empty list to store guesses
tries = 5  # player starts with 5 tries
correct_answer_picked = False  # false until they get it right

while not correct_answer_picked and tries > 0:  # keep going until they win or run out of tries
    print(f"You have {tries} tries remaining.")  # shows how many tries are left
    ask = int(input("Enter a number between 1 - 10: "))  # gets the guess and makes it an int

    while ask < 1 or ask > 10 or ask in previous_guesses:  # loops while the guess is bad
        if ask < 1 or ask > 10:  # checks if its out of range
            print("Invalid input!")  # tells them its invalid
        else:  # if its not out of range then its a repeat
            print(f"You already guessed {ask}!\nChoose a different number.")  # says they already guessed it
            print(f"Previous guesses: {previous_guesses}")  # shows the old guesses
        ask = int(input("Enter a number between 1 - 10: "))  # asks again

    previous_guesses.append(ask)  # adds the good guess to the list

    if ask == num:  # checks if the guess is right
        print(f"You guessed correctly! The number was {num}.")  # tells them they won
        print(f"Your guesses: {previous_guesses}")  # shows all their guesses
        correct_answer_picked = True  # sets to true so the loop stops
    elif ask > num:  # checks if the guess is too high
        print("Try again! The random number is lower!")  # tells them to go lower
        tries -= 1  # takes away a try
        print(f"Previous guesses: {previous_guesses}")  # shows the guesses so far
    else:  # if its not right or too high then its too low
        print("Try again! The random number is higher!")  # tells them to go higher
        tries -= 1  # takes away a try
        print(f"Previous guesses: {previous_guesses}")  # shows the guesses so far

if not correct_answer_picked:  # runs if they never got it right
    print("You ran out of tries!")  # tells them they ran out
    print(f"Your guesses were: {previous_guesses}")  # shows all their guesses
    print(f"The correct number was {num}.")  # reveals the number
    print("Game over!")  # ends the game
