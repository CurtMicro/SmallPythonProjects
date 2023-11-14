import random

max_range = input("Type a number: ")

if max_range.isdigit():
    max_range = int(max_range)

    if max_range <= 0:
        print("Please type a number > 0")
        quit()
else:
    print("Please type a number")
    quit()

random_number = random.randint(0, max_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number next time")
        continue

    if user_guess == random_number:
        print("You Got it!")
        break
    elif user_guess > random_number:
        print("You were above the Number!")
    else:
        print("You were below the Number!")

print("You got it in", guesses, "guesses")
