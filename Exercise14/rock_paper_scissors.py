import random

rock = 'rock'
paper = 'paper'
scissors = 'scissors'
valid_choices = [rock, paper, scissors]


def user_choice():
    user_input = input("Enter R for rock, P for paper or S for scissors: ")
    user_input.lower().strip()
    if user_input == 'r':
        user_input = rock
    if user_input == 'p':
        user_input = paper
    if user_input == 's':
        user_input = scissors
    return user_input


def computer_choice():
    random_number = random.randint(0, 2)
    if random_number == 0:
        return rock
    elif random_number == 1:
        return paper
    elif random_number == 2:
        return scissors
    else:
        return print('Something went wrong with this generate_computer_choice function')


def rock_paper_scissors_game():
    print("Hello and welcome to the Rock..Paper...Scissors game!\n"
          "Remember Rock smashes Scissors, Paper wraps Rock, Scissors cut Paper!\n")
    user_input = user_choice()
    computer_input = computer_choice()

    if user_input not in valid_choices:
        return print("You didn't enter R nor S nor P, I take it you don't want to play. Bye.")

    print(f"\nYour choice: {user_input}\nComputer choice: {computer_input}\n")

    if user_input == computer_input:
        print("You drew against the computer!")
    else:
        if user_input == rock:
            if computer_input == paper:
                print('Computer won!!!')
            else:
                print('You are the winner!!!')
        if user_input == paper:
            if computer_input == rock:
                print('You are the winner!!!')
            else:
                print('Computer won!!!')
        if user_input == scissors:
            if computer_input == rock:
                print('Computer won!!!')
            else:
                print('You are the winner!!!')

    print('\nGood game')

    play_again = input('\nWant to play again?\n Type Y for yes, otherwise type anything else: ')
    if play_again.lower().strip() == 'y':
        print('\nOkay! Here we go! \n')
        rock_paper_scissors_game()
    else:
        print('OK, bye :)')


rock_paper_scissors_game()
