import random

user_wins = 0
computer_wins = 0
draw = 0

options = ["rock", "paper", "scissors"]

while True:
    user_choice = input("Type Rock or Paper or Scissors to play or 'q' to quit: ").lower()
    if user_choice == 'q':
        break

    if user_choice not in options:
        print("Enter a valid choice: ")
        continue

    random_number = random.randint(0, 2)
    # 0 for rock, 1 for paper, 2 for scissors

    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_choice == computer_pick:
        print("It's a draw!")
        draw += 1
    elif user_choice == "rock" and computer_pick == "scissors":
        print("Rock smashes scissors! You win!")
        user_wins += 1
    elif user_choice == "paper" and computer_pick == "rock":
        print("Paper blocks Rock! You win!")
        user_wins += 1
    elif user_choice == "scissors" and computer_pick == "paper":
        print("Scissors cuts Paper! You win!")
        user_wins += 1
    else:
        print("Commputer wins!")
        computer_wins += 1

print("You won",user_wins,"times. ")
print("Computer won",computer_wins,"times. ")
print("Goodbye! ")