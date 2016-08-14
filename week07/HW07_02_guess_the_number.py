import random

MIN = 0
MAX = 10

def randomNum():
    return random.randrange(MIN, MAX, 1)

def check_guess(userGuess, compNum):
    if (userGuess == compNum):
        print("You won! The computer chose the number {} just like you guessed!".format(userGuess))
        return True
    elif (userGuess > 10 or userGuess < 0):
        print("The number the computer chose is between {} and {}. Your guess is out of range".format(MIN, MAX))
        return False
    elif ((userGuess < compNum)):
        print("The number the computer chose is larger than {}.".format(userGuess))
        return False
    elif (userGuess > compNum):
        print("The number the computer chose is smaller than {}.".format(userGuess))
        return False
    ## Does not deal with floats
    # else:
    #    print("The expression {} is not valid. The number the computer chose is {}".format(userGuess, compNum)

def game():
    compNum = randomNum()
    print("The computer chose a random integer between {} and {}. You have 3 guesses:".format(MIN, MAX))
    correct = False
    attempts = 0

    while (not correct) and (attempts < 3):
        userGuess = int(input("Which number did the computer choose? ".format(3 - attempts)))
        attempts += 1
        correct = check_guess(userGuess, compNum)

# Condition to keep playing until user types something other than "Y" or "y"
answer = "y"
while (answer == "y"):
    game()
    # lowercase and uppercase acceptable
    answer = input("Game Over\nPlay again? Y/N ").lower()