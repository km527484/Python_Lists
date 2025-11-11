import random

computer_guess = random.randint(1,20)
#print(computer_guess)

user_guess = int(input("Guess a number: "))
#print(user_guess)

if user_guess > computer_guess:
    print("Guess is too high")

if user_guess < computer_guess:
    print("Guess is too low")

if user_guess == computer_guess:
    print("Guess is correct!")

while user_guess != computer_guess:
    user_guess = int(input("Guess another number: "))
    if user_guess > computer_guess:
        print("Guess is too high")
    elif user_guess < computer_guess:
        print("Guess is too low")
else:
    print("Guess is correct!")