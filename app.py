# create a simple rock paper scissors game

import random

int_wins = 0
int_losses = 0
int_ties = 0

while True:
    print("select between rock, paper, scissors: ")
    str_user_in = input()
    str_user_in = str_user_in.lower()

    if not (str_user_in == "rock" or str_user_in == "paper" or str_user_in == "scissors"):
        print("invalid input")
        continue
    else:
        int_comp_in = random.randint(1, 3)
        if int_comp_in == 1:
            str_comp_in = "rock"
        elif int_comp_in == 2:
            str_comp_in = "paper"
        else:
            str_comp_in = "scissors"

        print("you chose " + str_user_in + " and the computer chose " + str_comp_in)

        if str_user_in == str_comp_in:
            print("it's a tie!")
            int_ties += 1
        elif str_user_in == "rock" and str_comp_in == "scissors":
            print("you win!")
            int_wins += 1
        elif str_user_in == "paper" and str_comp_in == "rock":
            print("you win!")
            int_wins += 1
        elif str_user_in == "scissors" and str_comp_in == "paper":
            print("you win!")
            int_wins += 1
        else:
            print("you lose!")
            int_losses += 1

        while True:
            print("play again?")
            str_play_again = input()
            str_play_again = str_play_again.lower()

            if str_play_again == "y" or str_play_again == "yes":
                break
            elif str_play_again == "n" or str_play_again == "no":
                print("thanks for playing!")
                print("wins: " + str(int_wins) + " losses: " + str(int_losses) + " ties: " + str(int_ties))
                exit()
            else:
                print("invalid input")
                continue
