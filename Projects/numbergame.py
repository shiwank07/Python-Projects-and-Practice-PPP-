import random

top_of_range = input("Please type a numebr: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a positive number.")
        quit()

else:
    print("Please type a number next type")
    quit()

random_number = random.randint(1, top_of_range)
print("Guess a number between 1 and " + str(top_of_range) + ":")

guesses = 0

while True:
    guesses += 1
    user_input = input("Make a guess: ")

    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("Please type a number next time.")
        continue

    if user_input == random_number:
        print(f"Yay, you've guessed it! The number was {random_number}")
        break
    else:
        if user_input < random_number:
            print("You are below the number! ")
        else:
            print("You are above the number! ")

print("You got it in", guesses,"guesses")
