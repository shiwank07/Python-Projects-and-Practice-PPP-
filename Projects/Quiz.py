print("Welcome to my quiz game!")

playing = input("Do yo want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0;

answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stands for? ")
if answer.lower() == "graphical processing unit":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

answer = input("What does WWW stands for? ")
if answer.lower() == "world wide web":
    print('Correct! ')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4) * 100) + "%.")


