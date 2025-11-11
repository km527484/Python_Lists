import random

play_again = True

my_list = ["rock", "paper", "scissors"]


while play_again:
    computer_guess = random.choice(my_list)
    user_guess = input("Guess rock, paper, or scissors: ")
    if computer_guess == user_guess:
        print("It's a tie!")
    elif user_guess == "rock":
        if computer_guess == "paper":
            print("The computer guessed paper. You lose!")
        else:
            print("The computer guessed scissors. You win!")
    elif user_guess == "scissors":
        if computer_guess == "paper":
            print("The computer guessed paper. You win!")
        else:
            print("The computer guessed rock. You lose!")
    elif user_guess == "paper":
        if computer_guess == "paper":
            print("The computer guessed rock. You win!")
        else:
            print("The computer guessed scissors. You lose!")
    else:
        print("Guess not valid")


    ask_again = str(input("Do you want to play again, yes or no? "))
    if ask_again == "no":
        play_again = False
    
