import random

BOOM = 7
MIN = 0
MAX = 1

#Produces 0 and 1 randomaly
def random_generator():
    return random.randint(MIN, MAX)


#0 becomes 1; 1 becomes 0
def next_player(player):
    return (player + 1) % 2


#Checks if the input is valid: Digits/ 'BOOM'
def valid_input(guess):
    if guess.upper() in ('BOOM', 'TRACH'):
        return True
    else:
        return guess.isdigit()


def computer_guess(current):
    next_number = current + 1
    if (next_number % BOOM == 0):
        print("The computer guessed: 'BOOM'")
    else:
        print("The computer guessed: {}".format(next_number))
    return next_number


def user_guess(current):
    guess = input("Your turn. Type in the next number, 'BOOM' or 'TRACH' ")
    next_number = current + 1
    valid = valid_input(guess)
    if not valid:
        print ('Game over. Invalid Input')
        return False
    elif (guess in ('TRACH', 'Trach', 'trach')) and (next_number % (2*BOOM) == 0):
        return next_number
    elif (guess in ('BOOM', 'Boom', 'boom')) and (next_number % BOOM == 0):
        return next_number
    elif (int(guess) == next_number) and (next_number % BOOM != 0):
        return next_number
    else:
        print ('Game over')
        return False



def play_game():
    print("Sheva Boom rules: Type in the next number. If it's a multiplication of {} - type 'BOOM'."
          " If it's a multiplication of {} - type 'TRACH'.".format(BOOM, BOOM*2))
    player = random_generator()
    if player == 0:
        current = random_generator()
        print("The computer was randomaly chosen to begin.\n"
              "The computer chose to begin with the number {}".format(current))
    else:
        print("You were randomly chosen to begin.\nYou can start the game with either 0 or 1.")
        try:
            current = int(input("How would you like to start? "))
        except ValueError:
            print("That's not valid")
    turns = 99
    while turns > 0:
        player = next_player(player)
        if player == 1:
            current = user_guess(current)
        else:
            current = computer_guess(current)
        turns -= 1
        if current == False:
            break
    return


# Condition to keep playing until user types something other than "Y" or "y"
answer = "y"
while (answer == "y"):
    play_game()
    # lowercase and uppercase acceptable
    answer = input("Play again? Y/N ").lower()