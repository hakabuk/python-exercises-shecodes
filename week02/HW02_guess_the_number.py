from random import randint

def game():
    # MIN and MAX as variables allow developer to change upper and lower bound fast
    MIN = 0
    MAX = 10
    compNum = randint(MIN,MAX)
    print("The computer chose a random integer between 0 and 10".format(MIN, MAX))

    # Does not deal with float numbers
    userGuess = int(input("Take a guess: Which number did the computer choose? "))

    if (userGuess == compNum):
        print("You won! The computer chose the number {} just like you guessed!".format(userGuess))
    elif (userGuess > 10 or userGuess < 0):
        print("The number the computer chose is between {} and {}. Your guess is out of range".format(MIN, MAX))
    elif ((userGuess < compNum)):
        print("The number the computer chose is larger than {}. The number the computer chose is {}".format(userGuess, compNum))
    elif (userGuess > compNum):
        print("The number the computer chose is smaller than {}. The number the computer chose is {}".format(userGuess, compNum))
    else:
        print("The expression {} is not valid. The number the computer chose is {}".format(userGuess, compNum))

# Condition to keep playing until user types something other than "Y" or "y"
answer = "y"
while (answer == "y"):
    game()
    # lowercase and uppercase acceptable
    answer = input("Game Over\nPlay again? Y/N ").lower()