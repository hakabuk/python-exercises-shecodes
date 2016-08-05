import random

MIN = 0
MAX = 10

def randomNum():
    return random.randrange(MIN, MAX, 1)

def check_guess(userGuess, compNum):
    if (userGuess == compNum):
        print("You won! The computer chose the number {} just like you guessed!".format(userGuess))
    elif (userGuess > 10 or userGuess < 0):
        print("The number the computer chose is between {} and {}. Your guess is out of range".format(MIN, MAX))
    elif ((userGuess < compNum)):
        print("The number the computer chose is larger than {}. The number the computer chose is {}".format(userGuess, compNum))
    elif (userGuess > compNum):
        print("The number the computer chose is smaller than {}. The number the computer chose is {}".format(userGuess, compNum))
    ## Does not deal with floats
    # else:
    #    print("The expression {} is not valid. The number the computer chose is {}".format(userGuess, compNum)

def game():
    compNum = randomNum()
    print("The computer chose a random integer between {} and {}".format(MIN, MAX))

    userGuess = int(input("Take a guess: Which number did the computer choose? "))
    check_guess(userGuess, compNum)

# Condition to keep playing until user types something other than "Y" or "y"
answer = "y"
while (answer == "y"):
    game()
    # lowercase and uppercase acceptable
    answer = input("Game Over\nPlay again? Y/N ").lower()